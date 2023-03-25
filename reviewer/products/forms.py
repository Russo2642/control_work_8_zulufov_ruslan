from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'image')
        labels = {
            'title': 'Название',
            'category': 'Категория',
            'description': 'Описание',
            'image': 'Картинка'
        }
