from django.db import models

# Create your models here.

class FarmOwner (models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    timeAdded = models.DateTimeField('date added')

class AnimalCharacteristics (models.Model):
    characteristicNum = models.IntegerField(default=0)
    animalType = models.CharField(max_length=100)
    animalColor = models.CharField(max_length=20)
    animalSex = models.CharField(max_length=1)
    animalAge = models.CharField(max_length=5)
    animalWeight = models.CharField(max_length=10)
    timeAdded = models.DateTimeField('date added')

class FarmLocation (models.Model):
    ownerId = models.UUIDField(primary_key=True)
    farmNumber = models.UUIDField(primary_key=False)
    farmAddress = models.CharField(max_length=200)
    farmCity = models.CharField(max_length=200)
    farmState = models.CharField(max_length=200)
    timeAdded = models.DateTimeField('date added')

class AnimalsOwned (models.Model):
    id = models.UUIDField(primary_key=True)
    ownderId = models.ForeignKey(FarmOwner, on_delete=models.CASCADE)
    animalName = models.CharField(max_length=200)
    characteristic = models.IntegerField(default=0)
    farmNumber = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    timeAdded = models.DateTimeField('date added')



