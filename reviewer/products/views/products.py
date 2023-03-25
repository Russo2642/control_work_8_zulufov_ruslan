from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from products.forms import ProductForm
from products.models import Product

from products.forms import ReviewForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDetailView(FormMixin, DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    form_class = ReviewForm


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    # def test_func(self):
    #     return self.request.user.has_perm('product.change_product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('index')
