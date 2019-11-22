from django.shortcuts import render, redirect
from homepage.models import FarmOwner
from homepage.views import login
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from homepage.forms import AddFarmForm
from django.core.cache import cache

def addAnimal(request):
    if not checkLoggedIn():
        return redirect('/login')
    else:
        farm_owners = FarmOwner.name
        context = {'farm_owner': farm_owners}
        return render(request, 'logged-in/add-animal.html', context)

def editAnimal(request):
    if not checkLoggedIn():
        return redirect('/login')
    else:
        farm_owners = FarmOwner.name
        context = {'farm_owner': farm_owners}
        return render(request, 'logged-in/edit-animal.html', context)

def viewAnimal(request):
    if not checkLoggedIn():
        return redirect('/login')
    else:
        farm_owners = FarmOwner.name
        context = { 'farm_owner': farm_owners}
        return render(request, 'logged-in/view-animal.html', context)

def viewAllAnimals(request):
    if not checkLoggedIn():
        return redirect('/login')
    else:
        user_id = cache.get('logged_in')
        logged_in_user = FarmOwner.objects.get(userId=user_id)
        return render(request, 'logged-in/view-all-animals.html', {'userName': logged_in_user.name})

def farmInformation(request):
    form_save_success = False
    form = AddFarmForm()
    if not checkLoggedIn():
        return redirect('/login')
    else:
        if request.method == 'POST':
            form = AddFarmForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False) # Save but not right away, want to add foreign key
                farm_owner = FarmOwner.objects.get(userId=cache.get('logged_in')) # Get user id from cache
                instance.farmOwner = farm_owner # Set foreign key to model instance
                instance.save()
                form_save_success = True
        
        return render(request, 'logged-in/farm-information.html', {'addfarmform': form, 'formSuccess': form_save_success})     

def checkLoggedIn():
    logged_in = cache.get('logged_in')
    if logged_in is None:
        return False
    return True
