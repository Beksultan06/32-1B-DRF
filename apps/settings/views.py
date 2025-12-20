from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.settings.models import Category, Models
from apps.settings.serailizers import CategorySerializer, ModelsSerializers

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelsAPIView(ListAPIView):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializers
