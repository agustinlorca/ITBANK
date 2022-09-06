from django.db import models

# Create your models here.
        
class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.CharField(max_length=30)
    branch_address_id = models.IntegerField()
    loan_id = models.ForeignKey("Prestamos.Prestamo", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        
    def __str__(self):
        return self.branch_name