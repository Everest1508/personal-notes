from django.contrib.auth.models import AbstractUser
from django.db import models
from .encryption import encrypt_data, decrypt_data, generate_user_salt


class User(AbstractUser):
    # Plain fields for database operations (will be encrypted in _encrypted_* fields)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    salt = models.CharField(max_length=255, blank=True, null=True, help_text="Random salt for user data encryption")
    
    # Encrypted fields (stored as encrypted strings)
    encrypted_name = models.TextField(blank=True, null=True)
    encrypted_email = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']
    
    def save(self, *args, **kwargs):
        # Generate salt if user is new
        if not self.salt:
            self.salt = generate_user_salt()
        
        # Encrypt sensitive data before saving
        if self.name:
            self.encrypted_name = encrypt_data(self.name, self.salt)
        if self.email:
            self.encrypted_email = encrypt_data(self.email, self.salt)
        
        # Keep plain email for authentication (needed for login)
        # In production, you might want to remove this and handle authentication differently
        super().save(*args, **kwargs)
    
    @property
    def decrypted_name(self):
        """Get decrypted name"""
        if self.encrypted_name and self.salt:
            try:
                return decrypt_data(self.encrypted_name, self.salt)
            except:
                # Fallback to plain name if decryption fails
                return self.name
        return self.name
    
    @property
    def decrypted_email(self):
        """Get decrypted email"""
        if self.encrypted_email and self.salt:
            try:
                return decrypt_data(self.encrypted_email, self.salt)
            except:
                # Fallback to plain email if decryption fails
                return self.email
        return self.email
    
    def __str__(self):
        return self.decrypted_email if hasattr(self, 'decrypted_email') else self.email
