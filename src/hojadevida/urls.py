from django.urls import path
from src.hojadevida.views import home_view, Content_create, Content_list

app_name = 'curriculum_module'

urlpatterns = [
    path('', home_view, name="home"),
    path('content/', Content_list.as_view(), name="listar_contenido"),
    path('content/add', Content_create.as_view(), name="crear_contenido"),
]
