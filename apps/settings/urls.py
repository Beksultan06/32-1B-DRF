from django.urls import path

from apps.settings.views import CategoryAPIView

urlpatterns = [
    path("category-list/", CategoryAPIView.as_view(), name='category-list')
]