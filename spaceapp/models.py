from django.db import models
from missions.models import Missions
# Create your models here.
class UserMessage(models.Model):
    message = models.TextField()
    mission = models.ForeignKey(Missions, on_delete=models.CASCADE, related_name = 'messages', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.message[:50]} (Message for {self.mission.name} from {self.created_at.strftime("%Y-%m-%d %H:%M:%S")})'
    