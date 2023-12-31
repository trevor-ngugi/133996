from django.urls import path
from . import views

urlpatterns = [
    
   path("", views.index, name="index"),
    #  path("homepage", views.homepage, name="home"),
   path("login", views.login_view, name="login"),
   path("logout", views.logout_view, name="logout"),
   #new login style format
   path("loginnew", views.loginstyle, name="login_style"),
   path("registernew", views.registerstyle, name="register_style"),
   path("loginhome", views.loginhome, name="login_home"),
   path("dentist-profile", views.dentistProfile, name="dentist_profile"),
   path("patient-profile", views.patientProfile, name="patient_profile"),
   path("update-profile", views.updateProfile, name="update_profile"),
   path("home-new", views.homeNew, name="home_new"),
   path("scan-images", views.scanImages, name="scan_images"),
   path("prediction", views.prediction, name="prediction"),
    #  path("login-page",views.login,name="login-page")
   #  twillio 
   path('register', views.register, name='register'),
   path('home', views.home, name='home'),
   path('otp/<str:uid>/', views.otpVerify, name='otp'),
   #crud
   path('view-patient', views.patient_list, name='patient-list'),
   path('create/', views.create_patient, name='create-patient'),
   path('edit/<int:patient_id>/', views.edit_patient, name='edit-patient'),
   path('delete/', views.delete_patient, name='delete-patient'),
 ]