from django.shortcuts import render
from django.shortcuts import render
from login.models import FarmOwner
from django.http import Http404


# Create your views here.
def index(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'homepage/homepage.html', context)

# def details(request, farm_user):
#     try: 
#         farm_owner = FarmOwner.username.get(pk=farm_user)
#     except FarmOwner.DoesNotExist:
#         raise Http404("User does not exist")
#     return render(request, 'homepage/homepage.html', { 'farm_owner': farm_owner})

