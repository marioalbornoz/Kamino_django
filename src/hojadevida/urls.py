from django.urls import path
from django.contrib.auth.decorators import login_required
from src.hojadevida.views import home_view, content_create, Content_list, content_list_view

app_name = 'curriculum_module'

urlpatterns = [
    # path('', login_required(home_view), name="home"),
    path('list/', login_required(Content_list.as_view()), name="listar_contenido"),
    path('add/', login_required(content_create), name="crear_contenido"),
    path('api/', login_required(content_list_view), name="api"),

]
