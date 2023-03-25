from django.views.generic import ListView

from products.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at', )
    paginate_by = 4
    paginate_orphans = 0
