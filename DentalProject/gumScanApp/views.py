from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, "authCustom/signUp.html")

def register_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page
    else:
        form = RegistrationForm()
    return render(request, "authCustom/register.html", {'form': form})

def login_request(request):
    return render(request, "authCustom/login.html")#

def home(request):
    return render(request, "home/home.html")
