from datetime import datetime, time

from django.contrib.sessions.models import Session
from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Autenticación de credenciales mediante token (authtoken)
    con tiempo de expiración.

    La hora de expiración diaria global está definida para las 19:00 horas.
    """
    token_expired = False

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token inválido.')
        
        if token is not None:
            if not token.user.is_active:
                raise exceptions.AuthenticationFailed('Usuario inactivo o eliminado.')
        
        current_time = timezone.localtime(timezone.now()).time()
        expiration_time = time(23, 59)  # Aquí puedes definir la hora de muerte diaria del token.
        
        # Cuenta regresiva para la muerte del token: no es visible al usuario, pero es útil para el desarrollador.
        remaining_time = datetime.combine(datetime.now().date(), expiration_time) - datetime.combine(datetime.now().date(), current_time)

        
        token_is_expired = current_time > expiration_time

        if token_is_expired:
            user = token.user
            self.token_expired = True
            # Delete all sessions for user
            all_sessions = Session.objects.filter(
                expire_date__gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    # auth_user_id is the primary key's user on the session
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            token.delete()
            raise exceptions.AuthenticationFailed('Token expirado. Se ha cerrado la sesión activa.')
        
        return token.user
    