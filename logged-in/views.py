from django.shortcuts import render, redirect
from django.core.cache import cache
from homepage.models import FarmOwner, FarmLocation, Animal
from homepage.forms import AddFarmForm, AddAnimalForm
from django.forms import ModelChoiceField


def addAnimal(request):
    form_save_success = False
    form = AddAnimalForm()
    if not checkLoggedIn():
        return redirect('/login')
    else:
        farm_location = FarmLocation.objects.filter(farmOwner_id=cache.get('logged_in'))
        if request.method == 'POST':
            form = AddAnimalForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                farm_id = FarmLocation.objects.get(farmName=form.cleaned_data['farmId'])
                instance.farmId = farm_id
                instance.save()
                form_save_success = True
                form = AddAnimalForm()
        return render(request, 'logged-in/add-animal.html', {'form': form,
                                                             'form_success': form_save_success,
                                                             'farm_location': farm_location})

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
        context = {'farm_owner': farm_owners}
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
                form = AddFarmForm()

        return render(request, 'logged-in/farm-information.html', {'addfarmform': form, 'formSuccess': form_save_success})

def helpPage(request):
    if not checkLoggedIn():
        return redirect('/login')
    else:
        return render(request, 'logged-in/help.html')

def checkLoggedIn():
    logged_in = cache.get('logged_in')
    if logged_in is None:
        return False
    return True

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.id
