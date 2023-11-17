from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm,PatientForm
from django.contrib.auth import login,authenticate,logout
from .models import Patient

#model imports
import os
import cv2
from PIL import Image
import numpy as np

import tensorflow as tf
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError

from django.core.files.storage import FileSystemStorage
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


#model prediction

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def predict(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag=cv2.imread(path)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((150, 150))

        test_image =np.expand_dims(resized_image, axis=0) 

        # load model
        model = tf.keras.models.load_model(os.getcwd() + '/model.h5')

        result = model.predict(test_image) 
        # ----------------
        # LABELS
        # Cat 0
        # Dog 1
        # Monkey 2
        # Parrot 3
        # Elephant 4
        # Bear 5
        # ----------------
        print("Prediction: " + str(np.argmax(result)))

        if (np.argmax(result) == 0):
            prediction = "Cat"
        elif (np.argmax(result) == 1):
            prediction = "Dog"
        elif (np.argmax(result) == 2):
            prediction = "Monkey"
        elif (np.argmax(result) == 3):
            prediction = "Parrot"
        elif (np.argmax(result) == 4):
            prediction = "Elephant"
        elif (np.argmax(result) == 5):
            prediction = "Bear"
        else:
            prediction = "Unknown"
        
        return TemplateResponse(
            request,
            "home/prediction.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "home/prediction.html",
            {"message": "No Image Selected"},
        )
