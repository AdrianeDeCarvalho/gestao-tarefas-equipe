from django.urls import path
from . import views

urlpatterns = [
    # O caminho '' aqui representa a página inicial
    path('', views.listar_tarefas, name='listar_tarefas'),
]
