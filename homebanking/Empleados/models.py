from django.db import models

# Create your models here.

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField()  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        
class DireccionEmpleado(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.TextField('Dirección', max_length=255, blank=False, null=False)
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    employee_id = models.ForeignKey(Empleado, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Dirección del empleado'
        verbose_name_plural = 'Direcciones de los empleados'