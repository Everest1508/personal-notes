from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TextNote
from .serializers import TextNoteSerializer


class TextNoteViewSet(viewsets.ModelViewSet):
    serializer_class = TextNoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TextNote.objects.filter(user=self.request.user)
