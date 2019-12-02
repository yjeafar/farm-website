from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.cache import cache
from django.core.paginator import Paginator
from django.forms import ModelChoiceField
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from homepage.models import FarmOwner, FarmLocation, Animal
from homepage.forms import AddFarmForm, AddAnimalForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def addAnimal(request):
    form_save_success = False
    form = AddAnimalForm()
    if not checkLoggedIn():
        return redirect('/login')
    else:
       # Animal.objects.all().delete()
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

class UpdateAnimal(SuccessMessageMixin, UpdateView):
    model = Animal
    form_class = AddAnimalForm
    template_name_suffix = '_update_form'
    template_name = 'logged-in/edit-animal.html'
    slug_field = 'animalId'
    slug_url_kwarg = 'animalId'
    pk_url_kwarg = 'animal_pk'
    context_object_name = 'post'
    success_message = 'Animal Updated Successfully!'
    success_url = '/logged-in/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
          

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
        farms = FarmLocation.objects.filter(farmOwner=logged_in_user)
        animal_list = Animal.objects.filter(farmId__in=farms)
        paginator = Paginator(animal_list, 4)
        page = request.GET.get('page')
        animals = paginator.get_page(page)
        return render(request, 'logged-in/view-all-animals.html', {'userName': logged_in_user.name,
                                                                   'animals': animals})

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
