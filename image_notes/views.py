from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ImageNote
from .serializers import ImageNoteSerializer


class ImageNoteViewSet(viewsets.ModelViewSet):
    serializer_class = ImageNoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ImageNote.objects.filter(user=self.request.user)
