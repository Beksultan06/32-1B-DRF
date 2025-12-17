from django.contrib import admin
from apps.settings.models import Category, Models

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['title']