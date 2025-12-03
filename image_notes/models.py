from django.db import models
from django.conf import settings


class ImageNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='image_notes')
    photo = models.ImageField(upload_to='image_notes/')
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return self.description[:50] if self.description else f"Image Note {self.id}"
