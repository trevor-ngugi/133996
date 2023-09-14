from django.urls import path
from . import views

urlpatterns = [
    
   path("", views.index, name="index"),
    #  path("homepage", views.homepage, name="home"),
   path("login", views.login_view, name="login"),
   path("logout", views.logout_view, name="logout"),
    #  path("login-page",views.login,name="login-page")
   #  twillio 
   path('register', views.register, name='register'),
   path('home', views.home, name='home'),
   path('otp/<str:uid>/', views.otpVerify, name='otp')
 ]