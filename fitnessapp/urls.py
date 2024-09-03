# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('diets/', views.diet_list, name='diet_list'),
]
