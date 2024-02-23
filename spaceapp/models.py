from django.db import models

# Create your models here.
class UserMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50], f'Message from {self.created_at.strftime("%Y-%m-%d %H:%m:%S")}'
    