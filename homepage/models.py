import uuid
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

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
    thumb = models.ImageField(default='media/media/no-image-available.jpg', upload_to='media/')
    timeAdded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Animal, self).save(*args, **kwargs)
        self.thumb = get_thumbnail(self.thumb, '400x300', quality=99).url
        super(Animal, self).save(*args, **kwargs)
