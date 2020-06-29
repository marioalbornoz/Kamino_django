from django.db import models
import uuid

# Create your models here.

class Alumno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=30)
    carrera = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
