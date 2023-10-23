from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('dentist', 'Dentist'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    medical_history = models.TextField() 
   

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

