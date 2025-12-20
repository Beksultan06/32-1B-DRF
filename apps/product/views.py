from django.shortcuts import render
from django.db.models import Prefetch
from django.core.cache import cache
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.product.models import ProductImage, Prouct
from apps.product.serializers import ProductSerializer
from apps.product.filters import ProductFilter
from apps.product.pagination import StandartPagination
from apps.product.cache import build_cache_key

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandartPagination
    filterset_class = ProductFilter
    search_fields = ("title", )
    ordering = ("-created_at")

    def get_queryset(self):
        images_qs = ProductImage.objects.order_by("sort", "id")
        return (
            Prouct.objects.filter(is_active=True).select_related("category")
            .prefetch_related(Prefetch("images", queryset=images_qs,
            to_attr='prefetched_iamges'))
        )
    
    def list(self, request, *args, **kwargs):
        key = build_cache_key("products:key", request)
        cached = cache.get(key)

        if cached is not None:
            return self.get_paginated_response(cached) if isinstance(cached. dict) and "result" in cached else super().list(request, *args, **kwargs)

        response = super().list(request, *args, **kwargs)

        cache.set(key, response.data, timeout=60)
        return response

class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        return (
            Prouct.objects
            .select_related("category")
            .prefetch_related("images")
        )

    def retrieve(self, request, *args, **kwargs):
        key = build_cache_key("prodcust:detail", request)
        cached = cache.get(key) 
        if cached is not None:
            return Response(cached)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(key, response.data, timeout=300)
        return response