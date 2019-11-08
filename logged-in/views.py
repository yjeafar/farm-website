from django.shortcuts import render, redirect
from homepage.models import FarmOwner
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from homepage.forms import ContactForm

def addAnimal(request):
    farm_owners = FarmOwner.name
    context = { 'farm_owner': farm_owners}
    return render(request, 'logged-in/add-animal.html', context)

def editAnimal(request):
    farm_owners = FarmOwner.name
    context = { 'farm_owner': farm_owners}
    return render(request, 'logged-in/edit-animal.html', context)

def viewAnimal(request):
    farm_owners = FarmOwner.name
    context = { 'farm_owner': farm_owners}
    return render(request, 'logged-in/view-animal.html', context)

def viewAllAnimals(request):
    farm_owners = FarmOwner.name
    context = { 'farm_owner': farm_owners}
    return render(request, 'logged-in/view-all-animals.html', context)

def farmInformation(request):
    return render(request, 'logged-in/farm-information.html')
