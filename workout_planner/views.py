from django.shortcuts import render

from .forms import WorkoutPlannerForm, WorkoutForm

# Create your views here.
def workout_planner(request):
    form = {}    
    form["request_method"] = str(request.method)
    
    if request.method == 'POST':    
        planner_form_class = WorkoutPlannerForm(request.POST)
        workout_form_class = WorkoutForm(request.POST)
        if planner_form_class.is_valid() and  workout_form_class.is_valid():
            planner_form_class.save()
            workout_form_class.save()            
        else:
            print("form not valid")            
            print(request.errors)
    elif (request.method == 'GET'):
        planner_form_class = WorkoutPlannerForm()
        workout_form_class = WorkoutForm()

    return render(request, "workout_planner/workout_planner_home.html", {"workout_form": workout_form_class, "planner_form": planner_form_class})
