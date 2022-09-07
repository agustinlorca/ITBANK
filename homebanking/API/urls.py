from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views


router = DefaultRouter()
router.register(r'Lista de Usuarios', views.UserViewSet, basename='Lista de Usuarios')
router.register(r'Informacion Cliente', views.ClienteViewSet, basename='Informacion Cliente')
router.register(r'Informacion Cuenta', views.CuentaViewSet, basename='Informacion Cuentas')
router.register(r'Prestamos', views.PrestamosViewSet, basename='Prestamos')
router.register(r'Prestamos por Sucursal', views.SucursalViewSet, basename='Prestamos por Sucursal')
router.register(r'Direcciones', views.DireccionesViewSet, basename='Direcciones')
router.register(r'Tarjetas', views.TarjetasViewSet, basename='Tarjetas')
router.register(r'Lista Tarjetas', views.TarjetasListViewSet, basename='Lista Tarjetas')
router.register(r'Sucursales', views.SucursalPublicaViewSet, basename='Sucursales')


urlpatterns = [
    path('', include(router.urls))
 ]