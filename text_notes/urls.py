from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextNoteViewSet

router = DefaultRouter()
router.register(r'', TextNoteViewSet, basename='text-note')

urlpatterns = [
    path('', include(router.urls)),
]

