from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()