from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "authCustom/signUp.html")

def register(request):
    return render(request, "authCustom/register.html")

def login(request):
    return render(request, "authCustom/login.html")
