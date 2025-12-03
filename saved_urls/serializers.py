from rest_framework import serializers
from .models import SavedURL


class SavedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedURL
        fields = ['id', 'title', 'link', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

