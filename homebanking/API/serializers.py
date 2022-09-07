from rest_framework import serializers
from Clientes.models import Cliente, DireccionCliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from Sucursales.models import Sucursal
from Tarjetas.models import Tarjetas
from django.contrib.auth.models import User

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ["customer_id", "customer_name", "customer_surname", "customer_DNI", "dob"]
        
        
class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cuenta
        fields = ["account_id", "balance", "iban", "tipo_cuenta"]      
        
class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sucursal
        fields = ["branch_id", "branch_number", "branch_name", "branch_address_id"]
        
class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    branch_id = SucursalSerializer()
      
    class Meta:
        model = Prestamo
        fields = ["loan_id", "loan_type", "loan_date", "loan_total", "branch_id"]
      
        
class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DireccionCliente
        fields = ["id_direccion", "direccion", "ciudad", "provincia", "pais"]
          
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "username"]
        
class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Tarjetas
        fields = ["numero", "cvv", "fecha_de_otorgamiento", "fecha_de_vencimiento", "tipo_de_tarjeta", "marca_tarjetas", "user"]