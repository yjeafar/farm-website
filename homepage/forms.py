from django import forms

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