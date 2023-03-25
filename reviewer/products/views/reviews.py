from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView

from products.forms import ReviewForm

from products.models import Review

from products.models import Product


class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = pk
            form.author = request.user
            form.save()
        return redirect(request.META.get('HTTP_REFERER'))


class ReviewUpdateView(UpdateView):
    template_name = 'products/product_detail.html'
    model = Review
    #form_class = ReviewForm
    fields = ['text', 'rating']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.product_id})

    # def test_func(self):
    #     return self.request.user == self.object.author


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.product_id})

    def test_func(self):
        return self.request.user == self.get_object().author
