from django.urls import path
from apps.product.views import (ProductListAPIView, ProductDetailAPIView
,ProductCreateAPIView, ProductImageCreateAPIView, ProductDeleteAPIView, 
ProductImageDeleteAPIView, ProductUpdateAPIView
)

urlpatterns = [
    path("", ProductListAPIView.as_view(), name='products'),
    path("create/", ProductCreateAPIView.as_view(), name='create-products'),
    path("create-image/", ProductImageCreateAPIView.as_view(), name='create-products-image'),
    path("<int:id>/", ProductDetailAPIView.as_view(), name='product-detail'),
    path("<int:id>/update/", ProductUpdateAPIView.as_view(), name='product-update'),
    path("<int:id>/delete/", ProductDeleteAPIView.as_view(), name='product-delete'),
    path("<int:id>/delete/images/", ProductImageDeleteAPIView.as_view(), name='product-image-delete')
]