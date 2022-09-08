from cgitb import text
from django.shortcuts import render,redirect
from django.urls import reverse
from Sucursales.models import Sucursal
from Clientes.models import Cliente
from .forms import PrestamoForm
from .models import Prestamo
from django.contrib.auth.decorators import login_required
from Cuentas.models import Cuenta


@login_required
def prestamo_view(request):
    
    if request.method == "POST":
        form =PrestamoForm(request.POST)
        
        if form.is_valid():
            cuenta_id = Cuenta.objects.filter(user_id=request.user.id).first()
            branch = Cliente.objects.filter(user_id=request.user.id).first()
            prestamo_id=Prestamo.objects.filter(user_id=request.user).first()
            prestamo = Prestamo()
            if  prestamo_id is None:
                prestamo.user=request.user
                prestamo.loan_type= form.cleaned_data['loan_type']
                prestamo.loan_date= form.cleaned_data['loan_date']
                prestamo.loan_total= form.cleaned_data['loan_total']
                prestamo.branch_id=branch.branch_id
                if cuenta_id.tipo_cuenta == "Classic" and prestamo.loan_total > 100000:
                    return redirect(reverse("prestamos_complete")+"?classic")
                elif cuenta_id.tipo_cuenta == 'Gold' and prestamo.loan_total > 300000:
                    return redirect(reverse("prestamos_complete")+"?gold")
                elif cuenta_id.tipo_cuenta == 'Black' and prestamo.loan_total > 500000:
                    return redirect(reverse("prestamos_complete")+"?black")
                else: 
                    prestamo.save()
                    cuenta_id.balance= cuenta_id.balance + prestamo.loan_total
                    cuenta_id.save()
                    return redirect(reverse("prestamos_complete")+"?aprobado")
            else:
                return redirect(reverse("prestamos_complete")+"?rechazado")
    form = PrestamoForm()
    return render (request, "Prestamos/prestamos.html", context={"form":form})

@login_required

def prestamos_complete(request):
    return render(request, "prestamos/complete.html",)