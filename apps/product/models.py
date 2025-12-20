from django.db import models
from apps.settings.models import Category, Models

class Prouct(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание товара')
    price = models.CharField(max_length=15, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

class ProductImage(models.Model):
    product = models.ForeignKey(Prouct, on_delete=models.CASCADE, related_name='img')
    image = models.ImageField(upload_to='products/')
    sort = models.PositiveIntegerField(default=0, verbose_name='Сортировка')

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продукта'