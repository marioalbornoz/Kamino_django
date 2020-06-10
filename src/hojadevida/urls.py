from django.urls import path
from django.contrib.auth.decorators import login_required
from src.hojadevida.views import home_view, Content_create, Content_list, content_list_view

app_name = 'curriculum_module'

urlpatterns = [
    path('', login_required(home_view), name="home"),
    path('content/', login_required(Content_list.as_view()), name="listar_contenido"),
    path('content/add', login_required(Content_create.as_view()), name="crear_contenido"),
    path('content/api', login_required(content_list_view), name="api"),

]
