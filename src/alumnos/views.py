from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from src.alumnos.models import Alumno

# Create your views here.

class listStudents(ListView):
    model = Alumno
    template_name = 'list_students.html'

class PerfilStudents(DetailView):
    model = Alumno
    context_object_name = 'obj'
    template_name = 'perfil_students.html'