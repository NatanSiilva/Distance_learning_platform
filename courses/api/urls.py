from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'courses'

urlpatterns = [
     path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
     path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
]
