from django.contrib import admin

from .models import FarmOwner, FarmLocation, AnimalCharacteristics, Animal

admin.site.register(FarmOwner)

admin.site.register(FarmLocation)

admin.site.register(AnimalCharacteristics)

admin.site.register(Animal)

