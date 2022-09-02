from django.db import models

# Create your models here.

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_DNI = models.IntegerField()
    dob = models.DateField()
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
        return self.customer_id