from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'completed', 'created_at']
    list_filter = ['completed', 'date', 'created_at']
    search_fields = ['title', 'user__email']
