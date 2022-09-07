from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views


router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user-detail')
router.register(r'cliente', views.ClienteViewSet, basename='data_cliente')
router.register(r'cuentas', views.CuentaViewSet, basename='cuentas')
router.register(r'prestamos', views.PrestamosViewSet, basename='prestamos')
router.register(r'Prestamos por Sucursal', views.SucursalViewSet, basename='Prestamos por Sucursal')
router.register(r'direcciones', views.DireccionesViewSet, basename='direcciones')
router.register(r'tarjetas', views.TarjetasViewSet, basename='tarjetas')
router.register(r'sucursales', views.SucursalPublicaViewSet, basename='sucursales')


urlpatterns = [
    path('', include(router.urls))
 ]