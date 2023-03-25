from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from products.forms import ProductForm
from products.forms import ReviewForm
from products.models import Product


class ProductCreateView(UserPassesTestMixin, CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.add_product')


class ProductDetailView(FormMixin, DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    form_class = ReviewForm


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.change_product')


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.has_perm('product.delete_product')
