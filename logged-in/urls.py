from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewAllAnimals, name='viewAllAnimals'),
    path('add-animal', views.addAnimal, name='addAnimal'),
    path('edit-animal/<uuid:animal_id>', views.editAnimal, name='editAnimal'),
    path('view-animal', views.viewAnimal, name='viewAnimal'),
    path('help', views.helpPage, name='helpPage'),
    path('farm-information', views.farmInformation, name='farmInformation'),
] 
