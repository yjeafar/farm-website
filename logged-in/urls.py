from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.loggedIn, name='loggedin'),
    path('add-animal', views.addAnimal, name='addAnimal'),
    path('add-animal', views.addAnimal, name='addAnimal'),
    path('add-animal', views.addAnimal, name='addAnimal'),
    
]
