from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from openai import OpenAI
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import VoiceNote
from .serializers import VoiceNoteSerializer, SummarizeRequestSerializer


class VoiceNoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoiceNoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return VoiceNote.objects.filter(user=self.request.user)
    
    @swagger_auto_schema(
        method='post',
        request_body=SummarizeRequestSerializer,
        responses={
            200: openapi.Response('Summary generated successfully', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'summary': openapi.Schema(type=openapi.TYPE_STRING, description='Generated summary from OpenAI'),
                }
            )),
            400: 'Bad request - Invalid data',
            500: 'Internal server error - OpenAI API error'
        },
        operation_description="Summarize a voice note using OpenAI API. Send the transcribed text in the request body."
    )
    @action(detail=True, methods=['post'])
    def summarize(self, request, pk=None):
        voice_note = self.get_object()
        
        # Validate request data
        serializer = SummarizeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        text = serializer.validated_data['text']
        
        # Get OpenAI API key from settings
        api_key = getattr(settings, 'OPENAI_API_KEY', None)
        if not api_key:
            return Response(
                {'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in settings.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        try:
            # Initialize OpenAI client
            client = OpenAI(api_key=api_key)
            
            # Call OpenAI API to summarize the text
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text concisely."},
                    {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            summary = response.choices[0].message.content.strip()
            
            # Save summary to voice note
            voice_note.summary = summary
            voice_note.save()
            
            return Response({
                'summary': summary
            })
            
        except Exception as e:
            return Response(
                {'error': f'Failed to generate summary: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
