from django import forms
from .models import UserMessage

class UserMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['message']
