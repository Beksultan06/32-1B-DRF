from rest_framework import serializers

from apps.settings.models import Category, Models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]

class ModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ['id', 'title', 'category']