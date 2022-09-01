from rest_framework import serializers
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ["customer_id", "customer_name", "customer_surname", "customer_dni", "dob", "branch_id"]
        
        
class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cuenta
        fields = ["account_id", "customer_id", "balance", "iban"]
        

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = ["loan_id", "loan_type", "loan_date", "loan_total", "customer_id"]