from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioElementViewSet

router = DefaultRouter()
router.register(r'audio_elements', AudioElementViewSet, basename='audio-elements')

urlpatterns = [
    path('', include(router.urls)),
]
