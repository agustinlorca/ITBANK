from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.


class RegisterForm(UserCreationForm):
   username = forms.CharField(label="Nombre de usuario",max_length=100)
   first_name = forms.CharField(label="Nombre completo",max_length=100)
   last_name = forms.CharField(label="Apellido",max_length=100)
   dni = forms.CharField(label="DNI", max_length=8)
   email = forms.CharField(label="Correo elctrónico",widget=forms.EmailInput)
   password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2=forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
   
   
   class Meta:
    model = User
    fields = ["username","first_name","last_name","dni","email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user