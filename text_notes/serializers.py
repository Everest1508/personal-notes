from rest_framework import serializers
from .models import TextNote


class TextNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNote
        fields = ['id', 'title', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

