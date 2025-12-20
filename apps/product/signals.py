from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.product.models import ProductImage, Prouct
from apps.product.cache import bump_products_ver
from apps.settings.models import Category

@receiver([post_save, post_delete], sender=Prouct)
def invalidate_products_cache(sender, instance, **kwargs):
    bump_products_ver()

@receiver([post_save, post_delete], sender=ProductImage)
def invalidate_products_images_cache(sender, instance, **kwargs):
    bump_products_ver()

@receiver([post_save, post_delete], sender=Category)
def invalidate_category_cache(sender, instance, **kwargs):
    bump_products_ver()