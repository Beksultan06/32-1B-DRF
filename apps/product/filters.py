import django_filters
from apps.product.models import Prouct

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr="lte")

    class Meta:
        model = Prouct
        fields = ("category", 'is_active')