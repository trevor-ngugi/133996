from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('add-patient/', views.add_patient, name='add-patient'),
    path('view-patients/', views.view_patients, name='view-patients'),
    path('edit-patient/<int:patient_id>/', views.edit_patient, name='edit-patient'),
    path('delete-patient/<int:patient_id>/', views.delete_patient, name='delete-patient'),
    path('prediction/', views.predict, name='predict'),
]