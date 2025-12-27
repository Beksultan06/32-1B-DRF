from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.product.views import ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("product-image", ProductImageViewSet, basename="product_images")

urlpatterns = [
    
]

urlpatterns += router.urls