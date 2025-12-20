from django.contrib import admin
from django.utils.html import format_html
from apps.product.models import Prouct, ProductImage

class ProdcutImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 
    fields = ("sort", "image", "image_preview")

    def image_preview(self, obj):
        if obj  and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:8px;" />', obj.image.url)
        return '-'
    image_preview.short_description = "Preview"

@admin.register(Prouct)
class ProuctAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', 'category', 'is_active']
    list_filter = ['id', 'title']
    search_fields = ('title', )
    inlines = (ProdcutImageInline, )
