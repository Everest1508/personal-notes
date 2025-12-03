from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SavedURL
from .serializers import SavedURLSerializer


class SavedURLViewSet(viewsets.ModelViewSet):
    serializer_class = SavedURLSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SavedURL.objects.filter(user=self.request.user)
