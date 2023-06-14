from rest_framework.routers import DefaultRouter
from ApiArriendosAlegria.views import (
    UsuarioViewSet,
    TrabajadorViewSet,
    TypeWorkerViewSet,
    RegionReadOnlyViewSet,
    ComunaReadOnlyViewSet,
    BancoViewSet,
    TipoCuentaBancariaViewSet,
    CuentaViewSet,
    PropietarioViewSet,
    PersonalidadJuridicaViewSet,
    PropiedadViewSet,
    TipoPropiedadViewSet,
    ArriendatarioViewSet,
    ArriendoViewSet,
    DetalleArriendoViewSet,
    ServiciosExtrasViewSet,
    GastoComunViewSet,
    ArriendoDepartamentoViewSet,
    ValoresGlobalesViewSet,
    ActualizarValorArriendoPropiedad,
    DashboardViewSet
    
)

router = DefaultRouter()

router.register(r'usuario', UsuarioViewSet, basename="usuario")
router.register(r'trabajador', TrabajadorViewSet, basename="trabajador")
router.register(r'tipo_trabajador', TypeWorkerViewSet, basename="tipo_trabajador")
router.register(r'regiones', RegionReadOnlyViewSet, basename="regiones")
router.register(r'comunas', ComunaReadOnlyViewSet, basename="comunas")
router.register(r'bancos', BancoViewSet, basename="bancos")
router.register(r'tipo_cuentas_bancos', TipoCuentaBancariaViewSet, basename="tipo_cuentas_bancos")
router.register(r'cuenta', CuentaViewSet, basename="cuenta")
router.register(r'propietario', PropietarioViewSet, basename="propietario")
router.register(r'personalidad_juridica', PersonalidadJuridicaViewSet, basename="personalidad_juridica")
router.register(r'propiedad', PropiedadViewSet, basename="propiedad")
router.register(r'tipo_propiedad', TipoPropiedadViewSet, basename="tipo_propiedad")
router.register(r'arrendatario', ArriendatarioViewSet, basename="arrendatario")
router.register(r'arriendo', ArriendoViewSet, basename="arriendo")
router.register(r'detalle_arriendo', DetalleArriendoViewSet, basename="detalle_arriendo")
router.register(r'servicios_extras', ServiciosExtrasViewSet, basename="servicios_extras")
router.register(r'gasto_comun', GastoComunViewSet, basename="gasto_comun")
router.register(r'arriendo_departamento', ArriendoDepartamentoViewSet, basename="arriendo_departamento")
router.register(r'valores_globales', ValoresGlobalesViewSet, basename="valores_globales")
router.register(r'actualizar_valor_arriendo_propiedad', ActualizarValorArriendoPropiedad, basename="actualizar_valor_arriendo_propiedad")
router.register(r'dashboard', DashboardViewSet, basename="dashboard")


urlpatterns = router.urls