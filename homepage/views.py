import pdb
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from homepage.models import FarmOwner
from homepage.forms import ContactForm, LoginForm, CreateAccountForm



def home(request):
    farm_owners = FarmOwner.name #change this once data is added to the database
    #context = { 'all_objects': all_objects}
    query_results = FarmOwner.objects.all()
    return render(request, 'homepage/home.html', {'query_results': query_results})

def login(request):
    create_account_form = CreateAccountForm() # Tab needs to show Create Account Form
    password_incorrect = False
    if (request.method) == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user_value = str(FarmOwner.objects.get(username__iexact=form.cleaned_data['username'])) # Returns string with user and pass
                if form.cleaned_data['password'] in user_value: # If the password is inside of the string
                    return redirect('/logged-in/')
                else:
                    form = LoginForm()
                    password_incorrect = True
            except:
                form = LoginForm()
                password_incorrect = True

    return render(request, 'homepage/login-page.html', {'loginForm': form, 'createAccountForm': create_account_form,
                                                        'password_incorrect': password_incorrect})

def createAccount(request):
    login_form = LoginForm()
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            response = redirect('/logged-in/')
            return response
    else:
        form = CreateAccountForm()

    return render(request, 'homepage/login-page.html', {'createAccountForm': form, 'loginForm': login_form})

def aboutMe(request):
    return render(request, 'homepage/about-me.html')

def contactMe(request):
    if (request.method) == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        sendEmail(form)
        return render(request, 'homepage/contact-me.html', {'form': form, 'successful_submit':True})
    return render(request, 'homepage/contact-me.html', {'form': form})

def sendEmail(form):
    if form.is_valid():
        subject = form.cleaned_data['subject']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, email, ['yjeafar@gmail.com'])
            form = ContactForm()
        except BadHeaderError:
            return HttpResponse('Invalid Header found.')
