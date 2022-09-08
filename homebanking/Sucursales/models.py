from random import choices
from django.db import models

# Create your models here.
        
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        
    def __str__(self):
        return self.branch_name