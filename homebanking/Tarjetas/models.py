from django.db import models

# Create your models here.
    
class Tarjetas(models.Model):
    numero = models.TextField(primary_key=True)
    cvv = models.TextField()  # Field name made lowercase.
    fecha_de_otorgamiento = models.TextField()
    fecha_de_vencimiento = models.TextField()
    tipo_de_tarjeta = models.TextField()
    marca_tarjetas = models.TextField(default="VISA")

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'