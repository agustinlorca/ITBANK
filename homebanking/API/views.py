from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from API.serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, UserSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
        