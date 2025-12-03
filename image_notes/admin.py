from django.contrib import admin
from .models import ImageNote


@admin.register(ImageNote)
class ImageNoteAdmin(admin.ModelAdmin):
    list_display = ['description', 'user', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['description', 'user__email']
