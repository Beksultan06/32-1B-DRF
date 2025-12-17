from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

class Models(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='model'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Модели'    