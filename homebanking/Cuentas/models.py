from django.db import models
from django.contrib.auth.models import User

# Create your models here.
       
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.TextField(default="Classic")

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        
    def __str__(self):
        return self.user.username
