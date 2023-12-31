from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profile,Patient
import random
from .helper import MessageHandler

from .forms import PatientForm

 # Create your views here.

def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")

def loginstyle(request):
    # login style page
    
    return render(request, "users/loginNew.html")

def registerstyle(request):
    # login style page
    
    return render(request, "users/registerNew.html")

def loginhome(request):
    return render(request, "users/logApp.html")

def dentistProfile(request):
    return render(request, "dentist/dProfile.html")

def patientProfile(request):
    return render(request, "patients/pProfile.html")

def updateProfile(request):
    return render(request, "world/updateProfle.html")

def homeNew(request):
    return render(request, "home/home.html")

def scanImages(request):
    return render(request, "world/scan.html")

def prediction(request):
    return render(request, "world/prediction.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out"
            })


def home(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        return HttpResponse(" verified.")
    else:
        return HttpResponse(" Not verified.")


def register(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        user=User.objects.create(username=request.POST['user_name'])
        otp=random.randint(1000,9999)
        profile=Profile.objects.create(user=user,phone_number=request.POST['phone_number'],otp=f'{otp}')
        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_whatsapp()
        else:
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
        red=redirect(f'otp/{profile.uid}/')
        red.set_cookie("can_otp_enter",True,max_age=600)
        return red  
    return render(request, '2factor/register.html')



def otpVerify(request,uid):
    if request.method=="POST":
        profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"2factor/otp.html",{'id':uid})
#crud functions
def patient_list(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'patients/list.html',context)


def create_patient(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-list')

    context = {
        'form': form,
    }
    return render(request, 'patients/create.html',context)


# def edit_patient(request, pk):
#     patient = Patient.objects.get(id=pk)
#     form = PatientForm(instance=patient)
    
#     if request.method == 'POST':
#         form = PatientForm(request.POST, instance=patient)
#         if form.is_valid():
#             form.save()
#             return redirect('patient-list')

#     context = {
#         'patient': patient,
#         'form': form,
#     }
#     return render(request, 'patients/edit.html',context)

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-list')

    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'patients/edit.html',context)


def delete_patient(request, pk):
    return render(request, 'patients/delete.html',context)
