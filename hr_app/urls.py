
from django.urls import path
from hr_app import views

urlpatterns = [
    path('hrdash/', views.hrHome_views,name='hr_dash'),
    path('post/', views.post_job_views,name='post_job'),
    path('candidate-details/<int:pk>/', views.candidate_views, name='candidate_details'),
]