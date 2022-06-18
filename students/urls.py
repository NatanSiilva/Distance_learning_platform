from django.urls import path
from . import views


urlpatterns = [
     path('register', views.StudentRegistrationView, name='student_registration'),
]