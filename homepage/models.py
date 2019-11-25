import uuid
from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class FarmOwner(models.Model):
    userId = models.CharField(primary_key=True, max_length=100, blank=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(6)])
    username = models.CharField(unique=True, max_length=12, validators=[MinLengthValidator(5)])
    timeAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % {self.username, self.password, self.userId}

class FarmLocation(models.Model):
    farmOwner = models.ForeignKey(FarmOwner, on_delete=models.CASCADE)
    farmName = models.CharField(unique=True, max_length=200)
    farmAddress = models.CharField(max_length=200)
    farmCity = models.CharField(max_length=200)
    farmState = models.CharField(max_length=200)
    timeAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.farmName)

class Animal(models.Model):
    animalId = models.CharField(primary_key=True, max_length=100, blank=True, default=uuid.uuid4)
    farmId = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    animalName = models.CharField(max_length=200)
    animalType = models.CharField(max_length=100)
    animalColor = models.CharField(max_length=20)
    animalSex = models.CharField(max_length=10)
    animalAge = models.CharField(max_length=5)
    animalWeight = models.CharField(max_length=10)
    thumb = models.ImageField(default='homepage/static/homepage/images/no-image-available.png', blank=True)
    timeAdded = models.DateTimeField(auto_now_add=True)
