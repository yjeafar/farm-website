from django import forms
from homepage.models import FarmOwner

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, 
                                 widget=forms.TextInput(
                                    attrs={
                                        'class': 'formUserName' }))
    subject = forms.CharField(required=True,
                                 widget=forms.TextInput(
                                    attrs={
                                        'class': 'formSubject' }))
    message = forms.CharField(widget=forms.Textarea(
                                    attrs={
                                        'class': 'formMessage' }))

class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                                 widget=forms.TextInput(
                                    attrs={
                                        'class': 'formUser' }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'formPassword'}))

class CreateAccountForm(forms.ModelForm):
    class Meta: #Meta is using formModel which uses the columns from the db
        model = FarmOwner
        fields = ('name', 'email', 'username', 'password', ) # Fields in model that will be added
        widgets = {

            'name' : forms.TextInput(
                attrs={
                    'class': 'formName'}),

            'email' : forms.EmailInput(
                attrs={
                    'class': 'formEmail'}),

            'username' : forms.TextInput(
                attrs={
                    'class': 'formUser'}),

            'password' : forms.PasswordInput(
                attrs={
                    'class': 'formPassword'}),
        }
