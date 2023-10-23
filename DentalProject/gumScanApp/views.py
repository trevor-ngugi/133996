from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm,PatientForm
from django.contrib.auth import login,authenticate,logout
from .models import Patient
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

def user_logout(request):
    logout(request)
    return redirect('index') 

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PatientForm()
    return render(request, "home/addPatient.html", {'form': form})

def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'home/viewPatient.html', {'patients': patients})

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('view-patients')  
    else:
        form = PatientForm(instance=patient)

    return render(request, 'home/editPatient.html', {'form': form, 'patient': patient})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('view-patients')  

    return render(request, 'home/deletePatient.html', {'patient': patient})
