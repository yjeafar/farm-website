from django.shortcuts import render, redirect
from homepage.models import FarmOwner
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from homepage.forms import ContactForm


# Create your views here.
def home(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'homepage/home.html', context)

def login(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'homepage/login-page.html', context)

def createAccount(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    context = { 'farm_owner': farm_owners}
    return render(request, 'homepage/login-page.html', context)

def aboutMe(request):
    return render(request, 'homepage/about-me.html')

def contactMe(request):
    if (request.method) == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['yjeafar@gmail.com'])
                form = ContactForm()
                return render(request, 'homepage/contact-me.html', {'form': form, 'successful_submit': True })
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')
    return render(request, 'homepage/contact-me.html', {'form': form})



# def details(request, farm_user):
#     try: 
#         farm_owner = FarmOwner.username.get(pk=farm_user)
#     except FarmOwner.DoesNotExist:
#         raise Http404("User does not exist")
#     return render(request, 'homepage/homepage.html', { 'farm_owner': farm_owner})

