from django import forms

from products.models import Product

from products.models import Review


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


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        required=True
    )

    class Meta:
        model = Review
        fields = ('text', 'rating')
        labels = {
            'rating': 'Оценка товара',
            'text': 'Текст комментария'
        }
