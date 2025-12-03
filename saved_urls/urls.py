from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavedURLViewSet

router = DefaultRouter()
router.register(r'', SavedURLViewSet, basename='saved-url')

urlpatterns = [
    path('', include(router.urls)),
]

