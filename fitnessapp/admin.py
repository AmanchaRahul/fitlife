from django.contrib import admin
from .models import Workout, Exercise, DietPlan

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(DietPlan)
