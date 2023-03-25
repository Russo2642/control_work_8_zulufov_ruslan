from django.urls import path

from products.views.base import IndexView

from products.views.products import ProductCreateView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
