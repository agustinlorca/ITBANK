from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views


router = DefaultRouter()
router.register(r'data_cliente', views.ClienteViewSet, basename='data_cliente')
router.register(r'cuentas', views.CuentaViewSet, basename='cuentas')
router.register(r'prestamos', views.PrestamosViewSet, basename='prestamos')


urlpatterns = [
    path('', include(router.urls))
 ]