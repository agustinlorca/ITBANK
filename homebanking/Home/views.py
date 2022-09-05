from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "home/home.html",)


@login_required

def main(request):
    return render(request, "home/main.html",)