from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views


router = DefaultRouter()
router.register(r'data_cliente', views.ClienteViewSet)
router.register(r'cuentas', views.CuentaViewSet)
router.register(r'prestamos', views.PrestamosViewSet)


urlpatterns = [
    path('', include(router.urls))
 ]