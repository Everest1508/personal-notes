from rest_framework import serializers
from .models import TextNote


class TextNoteSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = TextNote
        fields = ['id', 'title', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_title(self, obj):
        """Return decrypted title"""
        return obj.decrypted_title
    
    def get_description(self, obj):
        """Return decrypted description"""
        return obj.decrypted_description
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

