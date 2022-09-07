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
from rest_framework import status 
from Tarjetas.models import Tarjetas
from django.core.exceptions import PermissionDenied
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', "username"]

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

    def destroy(self, request, pk=None):
        if request.user.is_staff:
            cuenta = Cuenta.objects.filter(user_id=request.user.id).first()
            prestamo = Prestamo.objects.filter(user_id=request.user.id).first()
            cuenta.balance = cuenta.balance - prestamo.loan_total
            prestamo.delete()
            cuenta.save()
            return Response(f'Prestamo eliminado correctamente. Se reintegraron en la cuenta ${prestamo.loan_total} del prestamo solicitado.', status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    def create(self,request):
        if request.user.is_staff:
            cuenta_id = Cuenta.objects.filter(user_id=request.user.id).first()
            branch = Cliente.objects.filter(user_id=request.user.id).first()
            Prestamo.objects.create(
            user=request.user,
            loan_type=request.POST['loan_type'],
            loan_date=request.POST['loan_date'],
            loan_total=request.POST['loan_total'],
            branch_id=branch.branch_id
            )
            cuenta = Cuenta.objects.filter(user_id=request.user.id).first()
            prestamo = Prestamo.objects.filter(user_id=request.user.id).first()
            cuenta.balance = cuenta.balance + prestamo.loan_total
            prestamo.save()
            cuenta.save()
            if cuenta_id.tipo_cuenta == "Classic" and prestamo.loan_total > 100000:
                cuenta.balance = cuenta.balance - prestamo.loan_total
                prestamo.delete()
                cuenta.save()
                return Response({f'Error al solicitar el prestamo. El monto de ${prestamo.loan_total} supera el límite como cliente Classic, que es de $100.000 .'}, status=status.HTTP_200_OK)
            elif cuenta_id.tipo_cuenta == 'Gold' and prestamo.loan_total > 300000:
                cuenta.balance = cuenta.balance - prestamo.loan_total
                prestamo.delete()
                cuenta.save()
                return Response({f'Error al solicitar el prestamo. El monto de ${prestamo.loan_total} supera el límite como cliente Gold, que es de $300.000 .'}, status=status.HTTP_200_OK)
            elif cuenta_id.tipo_cuenta == 'Black' and prestamo.loan_total > 500000:
                cuenta.balance = cuenta.balance - prestamo.loan_total
                prestamo.delete()
                cuenta.save()
                return Response({f'Error al solicitar el prestamo. El monto de ${prestamo.loan_total} supera el límite como cliente Classic, que es de $100.000 .'}, status=status.HTTP_200_OK)
            else:
                return Response({f'Prestamo creado correctamente. Se depositaron en la cuenta los ${prestamo.loan_total} del prestamo solicitado.'}, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied
class DireccionesViewSet(viewsets.ModelViewSet):
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        direccion = DireccionCliente.objects.filter(user_id=user_id)
        return direccion

class SucursalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch_id']


class TarjetasViewSet(viewsets.ModelViewSet):
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
            user_id = self.request.user.id
            tarjetas = Tarjetas.objects.filter(user_id=user_id)
            return tarjetas
    
class TarjetasListViewSet(viewsets.ModelViewSet):
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Tarjetas.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    
class SucursalPublicaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch_id']
