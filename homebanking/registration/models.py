from django.db import models
from django.contrib.auth.models import User
from Clientes.models import Cliente

# Create your models here.

class Usuario(models.Model):
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()