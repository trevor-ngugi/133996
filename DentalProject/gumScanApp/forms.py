from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Patient



class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'role', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'email','medical_history'] 

