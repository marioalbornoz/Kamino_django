from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from src.alumnos.models import Alumno
from src.hojadevida.models import Curriculum
import uuid

# Create your views here.


class listStudents(ListView):
    model = Alumno
    template_name = 'list_students.html'


class PerfilStudents(DetailView):
    context_object_name = 'obj'
    template_name = 'perfil_students.html'

    def get_context_data(self, **kwargs):
        context = super(PerfilStudents, self).get_context_data(**kwargs)
        context['obj1'] = Curriculum.objects.all()
        print(" el contexto es ",context)
        return context
    def get_queryset(self):
        listaAlumnos = Alumno.objects.all()
        print( "alumnos :",listaAlumnos)
        return listaAlumnos


def contentcreate(request, pk):
    print("la pk entrante es", pk)
    if request.method == 'POST':
        form = request.POST.copy()
        content = form.get('content')
        Curriculum.objects.create(
            content=content, user_id=request.user.id, student_id=pk)
        return redirect('curriculum_module:listar_contenido')
    return render(request, 'form.html', context={"form": form})


class ContentListView(ListView):
    model = Curriculum
    template_name = 'perfil_students.html'
    context_object_name = 'curriculum'


# def contentlist(request):
#     obj1 = Curriculum.objects.all()
#     obj = Alumno.objects.all()
#     return render(request, "perfil_students.html", {'obj1':obj1, 'obj':obj})
