from django.db import models

import django.utils.timezone

# Create your models here.

class FarmOwner (models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    animalPictureFileType = models.CharField(max_length=10)
    timeAdded = models.DateTimeField(django.utils.timezone.now)

class AnimalCharacteristics (models.Model):
    characteristicNum = models.IntegerField(default=0)
    animalType = models.CharField(max_length=100)
    animalColor = models.CharField(max_length=20)
    animalSex = models.CharField(max_length=1)
    animalAge = models.CharField(max_length=5)
    animalWeight = models.CharField(max_length=10)
    timeAdded = models.DateTimeField(django.utils.timezone.now)

class FarmLocation (models.Model):
    farmOwner = models.ForeignKey(FarmOwner, on_delete=models.CASCADE)
    farmNumber = models.UUIDField(primary_key=False)
    farmAddress = models.CharField(max_length=200)
    farmCity = models.CharField(max_length=200)
    farmState = models.CharField(max_length=200)
    timeAdded = models.DateTimeField(django.utils.timezone.now)

class Animal (models.Model):
    ownderId = models.ForeignKey(FarmOwner, on_delete=models.CASCADE)
    animalName = models.CharField(max_length=200)
    characteristic = models.IntegerField(default=0)
    farmId = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    timeAdded = models.DateTimeField(django.utils.timezone.now)
