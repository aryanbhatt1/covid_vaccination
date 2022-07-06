from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import VaccinationCentre, city

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class VacinationCentreForm(ModelForm):
    class Meta:
        model = VaccinationCentre
        fields = [
            'centre_name',
            'address',
            'city',
            'pincode',

        ]

def cityChoices():
    return [(str(c), str(c)) for c in city.objects.all()]
    
class CityForm(forms.Form):
    city = forms.ChoiceField(choices=cityChoices())