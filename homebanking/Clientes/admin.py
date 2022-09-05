from django.contrib import admin
from .models import Cliente, DireccionCliente

# Register your models here.

admin.site.register(Cliente)
admin.site.register(DireccionCliente)