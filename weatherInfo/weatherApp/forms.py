from django.forms import ModelForm, TextInput
from .models import City
from django.contrib.auth.models import User
from django import forms
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class':'input', 'placeholder': 'City Name'})
        }

# forms.py




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

