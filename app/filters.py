import django_filters
from .models import House


class HouseFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = House
        fields = (
            'category',
            'address',
            'region',
            'area',
            'floor',
            'bedrooms',
            'bathrooms',
            'parking_lot',
            'is_security',
            'authorization_type'
        )