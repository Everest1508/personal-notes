from django.db import models
from django.conf import settings
from datetime import date
from authentication.encryption import encrypt_data, decrypt_data


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    # Encrypted fields
    encrypted_title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date', '-created_at']
    
    def save(self, *args, **kwargs):
        # Encrypt data using user's salt
        if self.user and self.user.salt:
            if self.title:
                self.encrypted_title = encrypt_data(self.title, self.user.salt)
        super().save(*args, **kwargs)
    
    @property
    def decrypted_title(self):
        """Get decrypted title"""
        if self.encrypted_title and self.user and self.user.salt:
            try:
                return decrypt_data(self.encrypted_title, self.user.salt)
            except:
                return self.title
        return self.title
    
    def __str__(self):
        return self.decrypted_title if hasattr(self, 'decrypted_title') else self.title
