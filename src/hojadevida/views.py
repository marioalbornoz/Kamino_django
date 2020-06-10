from django.shortcuts import render
from src.hojadevida.models import Curriculum
from django.http import HttpResponse, request, JsonResponse
from django.views.generic import CreateView, ListView
from src.hojadevida.forms import CurriculumForms
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib import admin

# Create your views here.

def home_views(request, *args, **kwargs):
    return HttpResponse("<h1> Hola Mundo </h1>")

def home_view(request, *args, **kwargs):
    return render(request, 'base.html', context={}, status=200)

class Content_create(CreateView):
    modelo = Curriculum
    form_class = CurriculumForms
    template_name = 'form.html'
    success_url = reverse_lazy('curriculum_module:listar_contenido')


class Content_list(ListView):
    model = Curriculum
    template_name = 'list_content.html'

def content_list_view(request, *args, **kwargs):
    qs = Curriculum.objects.all()
    notebook_list = [{"id": x.id, "user":x.user , "content": x.content, "created" :x.created, "updated": x.updated} for x in qs]
    data = {
        'isUser': True,
        'response': notebook_list
    }
    return JsonResponse(data)