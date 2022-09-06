from Clientes.models import Cliente, DireccionCliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from API.serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, UserSerializer, TarjetaSerializer, DireccionSerializer, SucursalSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from Sucursales.models import Sucursal
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from Tarjetas.models import Tarjetas

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        cliente = Cliente.objects.filter(user_id=user_id)
        return cliente
        
class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        cuenta = Cuenta.objects.filter(user_id=user_id)
        return cuenta
        
class PrestamosViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        prestamo = Prestamo.objects.filter(user_id=user_id)
        return prestamo
    
class DireccionesViewSet(viewsets.ModelViewSet):
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        direccion = DireccionCliente.objects.filter(user_id=user_id)
        return direccion

class SucursalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch_id']


class TarjetasViewSet(viewsets.ModelViewSet):
    serializer_class = TarjetaSerializer
    queryset = Tarjetas.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
    
class SucursalPublicaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch_id']
