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
        customer_id = self.request.user.id
        cliente = Cliente.objects.filter(customer_id=customer_id)
        return cliente
        
class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        customer_id = self.request.user.id
        cuenta = Cuenta.objects.filter(customer_id=customer_id)
        return cuenta
        
class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        