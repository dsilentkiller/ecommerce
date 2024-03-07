from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    #   <!--   widgets = {
    #         'name': forms.TextInput(attrs={'class': 'forms.control'}),

    #         'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'price': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'summer_coll': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'autmon_coll': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'hot_sell': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'discount': forms.TextInput(attrs={'class': 'forms.control'}),
    #         'created_at': forms.TextInput(attrs={'class': 'forms.control'}),

    #     } -->
