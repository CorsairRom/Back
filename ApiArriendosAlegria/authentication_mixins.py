from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header

from ApiArriendosAlegria.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    """
    Módulo base de autenticación de usuarios, que permite la autenticación
    mediante sistema de tokens de Django REST Framework.
    """
    user = None
    
    def get_user(self,request):
        """
        Retorna:
            * user      : Instancia de Usuario or 
            * message   : Mensaje de error or 
            * None      : Token dañado
        """
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None           
        
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            
            if user != None:
                self.user = user
                return user
        
        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')

        return (self.user, 1)