from django.shortcuts import  render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form =RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("register_complete")
		messages.error(request, "No se ha podido crear el registro. La información es inválida.")
	
	form = RegisterForm()
	return render (request, "registration/register.html",  context={"register_form":form})


def register_complete(request):
    return render(request, "registration/register_complete.html",)