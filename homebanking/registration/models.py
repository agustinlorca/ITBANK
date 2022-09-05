from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()