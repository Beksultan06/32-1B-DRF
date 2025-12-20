from django.urls import path
from apps.product.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name='products'),
    path("products/<int:id>/", ProductDetailAPIView.as_view(), name='product-detail')
]