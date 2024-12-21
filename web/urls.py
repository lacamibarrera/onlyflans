"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="landing"),
    path('acerca/', views.acerca, name="acerca"),
    path('bienvenido/', views.bienvenido, name="bienvenido"),
    path('contacto/', views.contacto, name="contacto"),
    path('exito/', views.exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reviews/', views.lista_reviews, name='lista_reviews'),
    path('flan/<slug:slug>/reviews/', views.flan_reviews, name='flan_reviews'), 
    path('flan/<slug:slug>/add_review/', views.add_review, name='add_review'),
    path('flan/<slug:flan_slug>/reseñas/', views.view_reviews, name='view_reviews'),
    path('cerrarsesion/', views.cerrarsesion, name="cerrarsesion"), 
    path('index/', views.index, name="index"),
]

