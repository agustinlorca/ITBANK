from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from registration.models import Usuario
from API.serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, UserSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        dni_usuario = self.request.user.username
        cliente = Cliente.objects.filter(customer_dni=dni_usuario)
        return cliente
        
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        