from django.contrib import admin

from products.models import Product

from products.models.review import Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'description', 'image')
    list_filter = ('id', 'title', 'category', 'description', 'image')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'rating')
    list_filter = ('id', 'author', 'product', 'text', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
