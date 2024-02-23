from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_missions , name='missions_page'),
    path('new', views.create_missions, name='new_mission'),
    #path('mission/details', views.mission_detail, name='mission_detail')
]
