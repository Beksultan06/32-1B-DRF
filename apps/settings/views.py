from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.settings.models import Category, Models
from apps.settings.serailizers import CategorySerializer, ModelsSerializers

class CategoryViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet
    ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelsViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet
    ):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializers