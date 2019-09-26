from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(results):
    return HttpResponse("Hello, world. This is the farms page!")

