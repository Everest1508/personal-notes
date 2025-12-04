from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ImageNote
from .serializers import ImageNoteSerializer


class ImageNoteViewSet(viewsets.ModelViewSet):
    serializer_class = ImageNoteSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]   # <-- REQUIRED

    def get_queryset(self):
        return ImageNote.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}
