from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
        read_only_fields = ['id']
    
    def get_name(self, obj):
        """Return decrypted name"""
        return obj.decrypted_name
    
    def get_email(self, obj):
        """Return decrypted email"""
        return obj.decrypted_email


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            username=validated_data['email']  # Use email as username
        )
        return user

