from django.urls import path, include

urlpatterns = [
    path('', include('ApiArriendosAlegria.routers'), name='trabajador_router'),
]
