from urllib import request
from django.shortcuts import render
from Tarjetas.models import Tarjetas
from Cuentas.models import Cuenta

# Create your views here.
def solicitar_tarjeta(request):
    return render(request, "tarjetas/solicitar_tarjeta.html",)


def tarjetas(request):
    user_id = request.user.id
    tarjeta = Tarjetas.objects.filter(user_id=user_id)
    cuenta = Cuenta.objects.filter(user_id=user_id)
    tarjeta_id=Tarjetas.objects.filter(user_id=request.user).first()
    if not tarjeta_id is None:
        return render(request, "Tarjetas/tarjetas.html",{'tarjetas':tarjeta,'cuentas':cuenta})
    else:
        return render(request, "Tarjetas/solicitar_tarjeta.html",)


