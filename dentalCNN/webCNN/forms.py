from django import forms
from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'contact', 'email', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-class-for-name'}),
            'contact': forms.TextInput(attrs={'class': 'custom-class-for-contact'}),
            'email': forms.EmailInput(attrs={'class': 'custom-class-for-email'}),
            'status': forms.Select(attrs={'class': 'custom-class-for-status'}),
        }