from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageNoteViewSet

router = DefaultRouter()
router.register(r'', ImageNoteViewSet, basename='image-note')

urlpatterns = [
    path('', include(router.urls)),
]

