from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.viewAllAnimals, name='viewAllAnimals'),
    path('add-animal', views.addAnimal, name='addAnimal'),
    path('edit-animal', views.editAnimal, name='editAnimal'),
    path('view-animal', views.viewAnimal, name='viewAnimal'),
    path('farm-information', views.farmInformation, name='farmInformation'),
]
