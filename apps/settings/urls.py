from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.settings.views import CategoryViewSet, ModelsViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet, basename='category')
router.register("models", ModelsViewSet, basename='models')

urlpatterns = [
    
]

urlpatterns += router.urls