from django.db import models
from django.conf import settings


class VoiceNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voice_notes')
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='voice_notes/')
    date = models.DateField()
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return self.title
