from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cuentas.models import Cuenta
# Create your views here.

def home(request):
    return render(request, "home/home.html",)


@login_required

def main(request):
    user_id = request.user.id
    cuenta = Cuenta.objects.filter(user_id=user_id)
    return render(request, "home/main.html",{'cuentas':cuenta})