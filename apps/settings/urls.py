from django.urls import path

from apps.settings.views import CategoryAPIView, ModelsAPIView

urlpatterns = [
    path("category-list/", CategoryAPIView.as_view(), name='category-list'), 
    path("model-list/", ModelsAPIView.as_view(), name='model-list'), 
]