from django.contrib import admin
from .models import Tarefa

# Register your models here.

@admin.register(Tarefa)
class TarefasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'prioridade', 'concluida')
    search_fields = ('titulo',)

