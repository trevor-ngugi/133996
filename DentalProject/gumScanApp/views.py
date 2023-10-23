from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login,authenticate,logout
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page
    else:
        form = LoginForm()
    return render(request, "authCustom/login.html",{'form': form})#

def home(request):
    return render(request, "home/home.html")
