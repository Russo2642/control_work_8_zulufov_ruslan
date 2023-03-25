from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False,
        null=False
    )
    commented_products = models.ManyToManyField(
        verbose_name='Отзыв на товары',
        to='products.Product',
        related_name='user_comments'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
