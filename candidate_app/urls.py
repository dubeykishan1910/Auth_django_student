from django.urls import path 
from candidate_app import views

urlpatterns = [
    path('candidate-dashbordh/', views.candidate_dashbordh, name='candidate_dashbordh'),
]
