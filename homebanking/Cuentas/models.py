from django.db import models
from Clientes.models import Cliente

# Create your models here.
       
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Cliente, models.DO_NOTHING)
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.TextField(default="Classic")

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        
    def __str__(self):
        return self.tipo_cuenta
