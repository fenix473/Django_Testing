from django.db import models
# Create your models here.

class Missions(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    launch_date = models.DateField()

class UserMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

