from django.db import models

# Create your models here.
        
class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'