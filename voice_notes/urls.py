from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoiceNoteViewSet

router = DefaultRouter()
router.register(r'', VoiceNoteViewSet, basename='voice-note')

urlpatterns = [
    path('', include(router.urls)),
]

