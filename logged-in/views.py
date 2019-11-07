from django.shortcuts import render, redirect
from homepage.models import FarmOwner
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from homepage.forms import ContactForm


def home(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'homepage/home.html', context)

def loggedIn(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'logged-in/login-page.html', context)

def addAnimal(request):
    farm_owners = FarmOwner.name
    context = { 'farm_owner': farm_owners}
    return render(request, 'add-animal/add-animal.html', context)
