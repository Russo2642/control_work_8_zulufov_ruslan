# Generated by Django 4.1.7 on 2023-03-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('category', models.CharField(choices=[('PHONE', 'Телефон'), ('COMPUTER', 'Компьютер'), ('TV', 'Телевизор'), ('CAMERA', 'Фото/Видео камера'), ('OTHER', 'Другое')], default='OTHER', max_length=20, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_pic', verbose_name='Картинка')),
            ],
        ),
    ]
