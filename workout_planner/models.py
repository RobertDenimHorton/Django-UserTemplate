from django.db import models
from users.models import Profile
# Create your models here.
class Workout(models.Model):
    workout_name = models.CharField(max_length=30)
    workout_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
              
    def __str__(self):
        return self.workout_name   
    
class WorkoutPlanner(models.Model):
    plan_name = models.CharField(max_length=30)
    plan_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    plan_workouts = models.ManyToManyField(Workout)
    
    def __str__(self):
        return self.plan_name 
        