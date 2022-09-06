from django.db import models

# Create your models here.

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=30)
    employee_surname = models.CharField(max_length=30)
    employee_hire_date = models.CharField(max_length=30)
    employee_dni = models.CharField(max_length=8, unique=True)  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class DireccionEmpleado(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    employee_id = models.ForeignKey(Empleado, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Dirección del empleado'
        verbose_name_plural = 'Direcciones de los empleados'