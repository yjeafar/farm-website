from django import forms
from homepage.models import FarmOwner, FarmLocation

STATES = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'),
          ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'),
          ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'),
          ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'),
          ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'),
          ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'),
          ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'),
          ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'),
          ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]


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

class AddFarmForm(forms.ModelForm):
    class Meta:
        model = FarmLocation
        fields = ('farmName', 'farmAddress', 'farmCity', 'farmState')
        labels = {
            'farmName': 'Farm Name',
            'farmCity': 'Farm City',
            'farmAddress': 'Farm Address',
            'farmState': 'Farm State'
        }
        widgets = {
            'farmName' : forms.TextInput(
                attrs={
                    'class': 'farmNameForm'
                }),
            'farmAddress' : forms.TextInput(
                attrs={
                    'class': 'farmAddressForm'
                }),
            'farmCity' : forms.TextInput(
                attrs={
                    'class': 'farmCityForm'
                }),
            'farmState' : forms.Select(choices=STATES,
                                       attrs={
                                           'class': 'farmStateForm'
                                           }),
        }
