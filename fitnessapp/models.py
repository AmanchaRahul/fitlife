# core/models.py

from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, choices=[('weight_gain', 'Weight Gain'), ('weight_loss', 'Weight Loss')])

    def __str__(self):
        return self.title

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='dietimages')
    category = models.CharField(max_length=50, choices=[('weight_gain', 'Weight Gain'), ('weight_loss', 'Weight Loss')])

    def __str__(self):
        return self.title

