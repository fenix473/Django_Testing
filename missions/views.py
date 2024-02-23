from django.shortcuts import render, redirect
from .models import Missions
from .forms import MissionForm
# Create your views here.

def view_missions(request):
    missions = Missions.objects.all()
    return render(request, 'missions.html', {'missions': missions})

def create_missions(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('missions_page')
        
    else:
        form = MissionForm()

    return render(request, 'new_mission.html', {'form': form})
