from django.contrib import admin
from .models import VoiceNote


@admin.register(VoiceNote)
class VoiceNoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'user__email']
