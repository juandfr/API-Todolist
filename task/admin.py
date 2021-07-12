from django.contrib import admin
from .models import Task

admin.site.site_header = 'Lista de Tarefas'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'description', 'created_at')
    search_fields = ('id', 'user_id')
    