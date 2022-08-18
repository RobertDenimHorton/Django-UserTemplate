from django.urls import path
from .views import workout_planner

urlpatterns = [
    path('workout_planner/', workout_planner, name='workout-planner'),
]
