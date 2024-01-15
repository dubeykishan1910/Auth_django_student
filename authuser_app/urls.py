from django.urls import path 
from authuser_app import views

urlpatterns = [
    path('candidate-register/', views.register_candidate, name='register_candidate'),
    path('hr-register/', views.register_hr, name='register_hr'),
]
