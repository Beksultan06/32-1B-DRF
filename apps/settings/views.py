from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.settings.models import Category
from apps.settings.serailizers import CategorySerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer