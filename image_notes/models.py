from django.db import models
from django.conf import settings
from authentication.encryption import encrypt_data, decrypt_data


class ImageNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='image_notes')
    photo = models.ImageField(upload_to='image_notes/')
    description = models.TextField()
    date = models.DateField()
    # Encrypted fields
    encrypted_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def save(self, *args, **kwargs):
        # Encrypt data using user's salt
        if self.user and self.user.salt:
            if self.description:
                self.encrypted_description = encrypt_data(self.description, self.user.salt)
        super().save(*args, **kwargs)
    
    @property
    def decrypted_description(self):
        """Get decrypted description"""
        if self.encrypted_description and self.user and self.user.salt:
            try:
                return decrypt_data(self.encrypted_description, self.user.salt)
            except:
                return self.description
        return self.description
    
    def __str__(self):
        desc = self.decrypted_description if hasattr(self, 'decrypted_description') else self.description
        return desc[:50] if desc else f"Image Note {self.id}"
