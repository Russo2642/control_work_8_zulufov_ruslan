from django.urls import path

from products.views.base import IndexView

from products.views.products import ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
