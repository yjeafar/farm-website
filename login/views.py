from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import FarmOwner

# Create your views here.
def index(results):
    farm_owners = FarmOwner.name #change this once data is added to the database
    template = loader.get_template('login/index.html') 
    context = {
        'farm_owner': farm_owners
    }
    return HttpResponse(template.render(context, results))
