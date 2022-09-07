from django import forms
from .models import Prestamo
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from django.contrib.auth.models import User

tipo = (
    ("HIPOTECARIO", "HIPOTECARIO"),
    ("PRENDARIO", "PRENDARIO"),
    ("PERSONAL", "PERSONAL"),
)


class PrestamoForm(forms.Form):
    loan_type = forms.ChoiceField(label="Tipo de prestamo *", choices=tipo)
    loan_date = forms.DateField(label="Fecha de inicio",initial=datetime.date.today)
    loan_total = forms.FloatField(label="Monto a solicitar *", max_value=1000000000000000)
    
    class Meta:
        model = Prestamo
        field = ['loan_type','loan_date','loan_total' ]