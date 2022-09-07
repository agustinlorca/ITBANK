from django.db import models
from django.contrib.auth.models import User
from Sucursales.models import Sucursal
# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_surname = models.CharField(max_length=30)
    customer_DNI = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    branch_id = models.ForeignKey(Sucursal, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}')
    

class DireccionCliente(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Direccion del Cliente'
        verbose_name_plural = 'Direcciones de los Clientes'
        
    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}')
        
