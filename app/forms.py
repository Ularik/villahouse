from django import forms
from .models import House


class HouseUpdateForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ('address', 'region', 'post_code', 'image', 'area',)


class HouseCreateForm(forms.ModelForm):

    class Meta:
        model = House
        fields = (
            'category',
            'address',
            'region',
            'post_code',
            'image',
            'area',
            'floor',
            'bedrooms',
            'bathrooms',
            'parking_lot',
            'description',
            'is_security',
            'authorization_type',
            'payment',
            'price',
            'is_active',

        )