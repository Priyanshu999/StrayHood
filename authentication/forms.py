from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User, Normal, NGO, Doctor

# User signup form same for all types of users
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
SEX_FEMALE = 'F'
SEX_MALE = 'M'
SEX_UNSURE = 'U'

SEX_OPTIONS = (
    (SEX_FEMALE, 'Female'),
    (SEX_MALE, 'Male'),
    (SEX_UNSURE, 'Unsure')
)

class NormalProfileForm(forms.ModelForm):
    class Meta():
        model = Normal
        sex= forms.ChoiceField(choices=SEX_OPTIONS),
        fields = ['name', 'age', 'contact', 'sex', 'address', 'profile_pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }


class NGOProfileForm(forms.ModelForm):
    class Meta():
        model = NGO
        fields = ['name', 'contact', 'address', 'profile_pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }


class DoctorProfileForm(forms.ModelForm):
    class Meta():
        model = Doctor
        sex =  forms.ChoiceField(choices=SEX_OPTIONS),
        fields = ['name', 'age', 'contact', 'sex', 'address', 'hospital', 'qualification', 'profile_pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),

        }













