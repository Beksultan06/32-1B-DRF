from rest_framework import serializers

from apps.product.models import Prouct, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'sort']

class ProductSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Prouct
        fields = ("id", 'title', 'description', 'price', 'category_title', "images", 'created_at')