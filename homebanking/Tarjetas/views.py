from django.shortcuts import render
from Tarjetas.models import Tarjetas
from Cuentas.models import Cuenta
# Create your views here.

def tarjetas(request):
    user_id = request.user.id
    tarjeta = Tarjetas.objects.filter(user_id=user_id)
    cuenta = Cuenta.objects.filter(user_id=user_id)
    return render(request, "Tarjetas/tarjeta.html",{'tarjetas':tarjeta,'cuentas':cuenta})
