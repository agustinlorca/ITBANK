"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views as home_views
from registration import views
from Prestamos import views as prestamo_view
from Tarjetas import views as tarjetas_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_views.home, name="home"),
    path('accounts/profile', home_views.main, name="mains"),
    path('accounts/',include('django.contrib.auth.urls')),
    path("register/", views.register_request, name="register"),
    path("register_complete/", views.register_complete, name="register_complete"),
    path("accounts/prestamos/", prestamo_view.prestamo_view, name="prestamo"),
    path("prestamos_complete", prestamo_view.prestamos_complete, name="prestamos_complete"),
    path("accounts/tarjetas/", tarjetas_view.tarjetas, name="tarjeta"),
    path("api/", include("API.urls"), name="api")
]
