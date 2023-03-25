from django.contrib.auth import get_user_model
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='reviews',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    product = models.ForeignKey(
        to='products.Product',
        related_name='reviews',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    text = models.TextField(
        null=False,
        blank=False,
        max_length=3000,
        verbose_name='Текст'
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Оценка'
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.author} - {self.product}"
