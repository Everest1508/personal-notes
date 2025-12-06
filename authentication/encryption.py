from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os
from django.conf import settings


def get_encryption_key():
    """
    Get or generate encryption key from settings
    """
    secret_key = getattr(settings, 'ENCRYPTION_SECRET_KEY', None)
    if not secret_key:
        # Generate a key from Django's SECRET_KEY if ENCRYPTION_SECRET_KEY is not set
        secret_key = settings.SECRET_KEY
    
    # Derive a 32-byte key from the secret key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'personal_notes_salt',  # Fixed salt for key derivation
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(secret_key.encode()))
    return key


def encrypt_data(data, user_salt):
    """
    Encrypt data using user-specific salt and secret key
    """
    if not data:
        return data
    
    # Combine secret key with user salt for unique encryption per user
    encryption_key = get_encryption_key()
    
    # Create a key specific to this user by combining with their salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=user_salt.encode() if isinstance(user_salt, str) else user_salt,
        iterations=100000,
        backend=default_backend()
    )
    user_key = base64.urlsafe_b64encode(kdf.derive(encryption_key))
    
    fernet = Fernet(user_key)
    encrypted_data = fernet.encrypt(data.encode() if isinstance(data, str) else data)
    return base64.urlsafe_b64encode(encrypted_data).decode()


def decrypt_data(encrypted_data, user_salt):
    """
    Decrypt data using user-specific salt and secret key
    """
    if not encrypted_data:
        return encrypted_data
    
    try:
        # Combine secret key with user salt for unique decryption per user
        encryption_key = get_encryption_key()
        
        # Create a key specific to this user by combining with their salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=user_salt.encode() if isinstance(user_salt, str) else user_salt,
            iterations=100000,
            backend=default_backend()
        )
        user_key = base64.urlsafe_b64encode(kdf.derive(encryption_key))
        
        fernet = Fernet(user_key)
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
        decrypted_data = fernet.decrypt(encrypted_bytes)
        return decrypted_data.decode()
    except Exception as e:
        # If decryption fails, return original data (for migration purposes)
        return encrypted_data


def generate_user_salt():
    """
    Generate a random salt for a user
    """
    return base64.urlsafe_b64encode(os.urandom(16)).decode()

