from django import forms
from .models import Missions

class MissionForm(forms.ModelForm):
    class Meta:
        model = Missions
        fields = ['name', 'description','launch_date']
