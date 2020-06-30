from django.shortcuts import render, redirect
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

def content_create(request):
    if request.method == 'POST':
        form = request.POST.copy()
        content = form.get('content')
        Curriculum.objects.create(content = content, user_id = request.user.id)
        return redirect('curriculum_module:listar_contenido')
    return render(request, 'form.html', context = {"form":form})

    # form = CurriculumForms(request.POST or None)
    # next_url = request.POST.get("next") or None
    # print("next_url", next_url)
    # if form.is_valid():
    #     #form.instance.id = request.user.id
    #     obj = form.save(commit=False)
    #     obj.save()
    #     if next_url != None:
    #         return redirect(next_url)
    #     form = CurriculumForms()
    # return render(request, 'form.html', context={"form":form})


class Content_list(ListView):
    model = Curriculum
    ordering = ['-created']
    template_name = 'list_content.html'

def content_list_view(request, *args, **kwargs):
    if request.user.id == 1:
        print("you are admin")
        qs = Curriculum.objects.all()
        notebook_list = [{"alumno_id":x.student.id ,"content_id": x.id, "content": x.content,"user_id":x.user_id , "created" :x.created, "updated": x.updated} for x in qs]
        data = {
            'isUser': False,
            'response': notebook_list
        }
        return JsonResponse(data)
    else:
        print("you are not admin")
        user_model_id = request.user.id
        qs = Curriculum.objects.filter(user_id = user_model_id)
        notebook_list = [{'Alumno_id':x.student.id ,"content_id": x.id, "content": x.content, "user_id":x.user_id ,"created" :x.created, "updated": x.updated} for x in qs]
        data = {
            'isUser': False,
            'response': notebook_list
        }
        return JsonResponse(data)
