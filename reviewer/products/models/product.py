from django.db import models


class CategoryChoice(models.TextChoices):
    PHONE = 'PHONE', 'Телефон'
    COMPUTER = 'COMPUTER', 'Компьютер'
    TV = 'TV', 'Телевизор',
    CAMERA = 'CAMERA', 'Фото/Видео камера',
    OTHER = 'OTHER', 'Другое'


class Product(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    category = models.CharField(
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER,
        max_length=20,
        verbose_name='Категория',
        null=False
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=3000,
        verbose_name='Описание'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='product_pic',
        verbose_name='Картинка'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
