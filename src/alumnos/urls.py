from django.urls import path
from django.contrib.auth.decorators import login_required
from src.alumnos.views import listStudents, PerfilStudents

app_name = 'alumno'

urlpatterns = [
    # path('', login_required(home_view), name="home"),
    path('', login_required(listStudents.as_view()), name="lista"),
    path('/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', login_required(PerfilStudents.as_view()), name="detalles"),
    # path('api', login_required(content_list_view), name="api"),

]
 