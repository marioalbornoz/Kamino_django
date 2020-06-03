from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.

class Curriculum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.content