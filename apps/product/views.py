from django.db.models import Prefetch
from django.core.cache import cache

from apps.product.models import ProductImage, Prouct
from apps.product.serializers import ProductSerializer, ProductImageSerializer
from apps.product.filters import ProductFilter
from apps.product.pagination import StandartPagination
from apps.product.cache import build_cache_key

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

class ProductViewSet(
        GenericViewSet, 
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    serializer_class = ProductSerializer
    pagination_class = StandartPagination
    filterset_class = ProductFilter
    search_fields = ("title", )
    ordering = ("-created_at", )
    lookup_field = "id"

    def get_queryset(self):
        images_qs = ProductImage.objects.order_by("sort", "id")
        return (
            Prouct.objects
            .filter(is_active=True)
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=images_qs,
                    to_attr="prefetched_images",
                )
            )
        )
        
    def list(self, request, *args, **kwargs):
        key = build_cache_key("products:list", request)
        cached = cache.get(key)
        if cached is not None:
            return Response(cached)

        response = super().list(request, *args, **kwargs)
        cache.set(key, response.data, timeout=60)
        return response
    
    def retrieve(self, request, *args, **kwargs):
        key = build_cache_key("product:detail", request)
        cached = cache.get(key)
        if cached is not None:
            return Response(cached)

        response = super().list(request, *args, **kwargs)
        cache.set(key, response.data, timeout=300)
        return response        

    def perform_create(self, serializer):
        serializer.save()
        cache.delete_pattern("products:*")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete_pattern("products:*")

    def perform_destroy(self, instance):
        instance.save()
        cache.delete_pattern("products:*")

class ProductImageViewSet(
        GenericViewSet, 
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete_pattern("products:*")