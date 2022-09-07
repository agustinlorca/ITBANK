from django.db import models
from django.contrib.auth.models import User
from Sucursales.models import Sucursal

# Create your models here.

class Prestamo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=30)
    loan_date = models.DateField(null=True, blank=True)
    loan_total = models.IntegerField()
    branch_id = models.ForeignKey(Sucursal, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        
    def __str__(self):
        return self.user.username