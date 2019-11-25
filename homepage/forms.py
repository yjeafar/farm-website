from django import forms
from homepage.models import FarmOwner, FarmLocation, Animal
from django.core.cache import cache

STATES = [('', 'Select State'), ('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'),
          ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'),
          ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'),
          ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'),
          ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'),
          ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'),
          ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'),
          ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'),
          ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]

ANIMAL_TYPE = [('dog', 'Dog'), ('cat', 'Cat'), ('sheep', 'Sheep'), ('horse', 'Horse'), ('goat', 'Goat'),
               ('cow', 'Cow'), ('chicken', 'Chicken'), ('pig', 'Pig'), ('mule', 'Mule'),
               ('duck', 'Duck')]

ANIMAL_SEX = [('male', 'Male'), ('female', 'Female'), ('N/A', 'N/A')]

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
                                           'class': 'form-control'
                                           }),
        }

class AddAnimalForm(forms.ModelForm):
    ANIMAL_TYPE.sort()
    ANIMAL_TYPE.append(('other', 'Other'))
    ANIMAL_TYPE.insert(0, ('', 'Select Animal Type'))
    farmId = forms.models.ModelChoiceField(queryset=FarmLocation.objects.filter(farmOwner_id=cache.get('logged_in')),
                                           empty_label=None,
                                           label="Name of Farm",
                                           widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = Animal
        fields = ('farmId', 'animalName', 'animalType', 'animalColor', 'animalAge', 'animalSex',
                  'animalWeight', 'thumb')
        labels = {
            'animalName': 'Animal Name',
            'animalType': 'Animal Type',
            'animalColor': 'Animal Color',
            'animalAge': 'Animal Age (Approx Years)',
            'animalSex': 'Animal Sex',
            'animalWeight': 'Animal Weight (Pounds)',
            'thumb': 'Picture of Animal'
        }
        widgets = {
            'animalName' : forms.TextInput(
                attrs={
                    'class': 'animalNameForm'
                }),
            'animalType' : forms.Select(choices=ANIMAL_TYPE,
                                        attrs={
                                            'class': 'form-control'
                                            }),
            'animalColor' : forms.TextInput(
                attrs={
                    'class': 'animalColorForm'
                }),
            'animalAge' : forms.NumberInput(
                attrs={
                    'min' : '0',
                    'class': 'animalAgeForm'
                }),
            'animalSex' : forms.RadioSelect(choices=ANIMAL_SEX,
                                            attrs={
                                                'class': 'animalSexForm',
                                            }),
            'animalWeight' : forms.NumberInput(
                attrs={
                    'min' : '0',
                    'class': 'animalWeightForm'
                }),
        }
