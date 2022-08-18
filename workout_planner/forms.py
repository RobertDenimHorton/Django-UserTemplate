from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import Profile

from .models import Workout, WorkoutPlanner

class WorkoutPlannerForm(forms.ModelForm):
    plan_name = forms.CharField(max_length=100)
    plan_author = forms.ModelChoiceField(queryset=None, empty_label=None)
    plan_workouts = forms.ModelMultipleChoiceField(queryset=None)
    class Meta:
        model = WorkoutPlanner
        fields = ['plan_name', 'plan_author', 'plan_workouts']
            
class WorkoutForm(forms.ModelForm):
    workout_name = forms.CharField(max_length=100)
    plan_author = forms.ModelChoiceField(queryset=None, empty_label=None)
    plan_workouts = forms.ModelMultipleChoiceField(queryset=None)
    class Meta:
        model = Workout
        fields = ['workout_name', 'workout_author']  

        
 
        
    