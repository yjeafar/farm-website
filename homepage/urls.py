from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('create-account/', views.createAccount, name="createAccont"),
    path('about-me/', views.aboutMe, name="aboutMe"),
    path('contact-me/', views.contactMe, name="contactMe"),
]
