from rest_framework import serializers
from .models import SavedURL


class SavedURLSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    
    class Meta:
        model = SavedURL
        fields = ['id', 'title', 'link', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_title(self, obj):
        """Return decrypted title"""
        return obj.decrypted_title
    
    def get_link(self, obj):
        """Return decrypted link"""
        return obj.decrypted_link
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

