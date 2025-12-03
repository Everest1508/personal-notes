from rest_framework import serializers
from .models import VoiceNote


class VoiceNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceNote
        fields = ['id', 'title', 'audio', 'date', 'summary', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class SummarizeRequestSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, help_text="The transcribed text from the audio to summarize")

