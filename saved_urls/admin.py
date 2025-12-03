from django.contrib import admin
from .models import SavedURL


@admin.register(SavedURL)
class SavedURLAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'user', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'link', 'user__email']
