from django.db import models

# Create your models here.

class Curriculum(models.Model):
    content = models.TextField(max_length = 1000)

    