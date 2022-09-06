from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_DNI = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    branch_id = models.IntegerField()   

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return self.customer_name
    

class DireccionCliente(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Direccion del Cliente'
        verbose_name_plural = 'Direcciones de los Clientes'
        
    def __str__(self):
        return self.direccion
        
