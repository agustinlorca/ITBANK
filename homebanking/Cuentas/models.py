from django.db import models
from django.contrib.auth.models import User

# Create your models here.
       
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.CharField(max_length=20)
    tipo_cuenta = models.CharField(max_length=20, default="Classic")

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        
    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}')
