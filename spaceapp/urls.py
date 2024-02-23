from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message_view , name='message_form'),
    path('message/success/', views.message_success, name='message_success'),
    path('messages/', views.view_messages, name = 'view_messages')
]

