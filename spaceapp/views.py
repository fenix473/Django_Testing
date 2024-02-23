from django.shortcuts import render, redirect
from spaceapp.forms import UserMessageForm
from .models import UserMessage

# Create your views here.
def message_view(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_success')

    else:
        form = UserMessageForm()
    return render(request,'message_form.html', {'form': form})

def message_success(request):
    return render(request, 'message_success.html')

def view_messages(request):
    messages = UserMessage.objects.all().order_by('-created_at')
    return render(request, 'view_messages.html',{'messages': messages})