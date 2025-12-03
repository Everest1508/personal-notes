from django.contrib import admin
from .models import TextNote


@admin.register(TextNote)
class TextNoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'description', 'user__email']
