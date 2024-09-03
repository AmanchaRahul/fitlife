from django.shortcuts import render, get_object_or_404
from .models import Workout, DietPlan

def home(request):
    return render(request, 'home.html')

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout_list.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    return render(request, 'workout_detail.html', {'workout': workout})

def diet_list(request):
    diet_plans = DietPlan.objects.all()
    return render(request, 'diet_list.html', {'diet_plans': diet_plans})
