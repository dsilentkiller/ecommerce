from django.db.models.query import QuerySet
from django.shortcuts import render
# from django.views.generic import ListView
from product.models import Product
from django.views.generic import ListView, DetailView, CreateView
from product.forms import ProductForm
# CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
# Create your views here.


def Base(request):
    return render(request, 'product/base.html')


class ProductListView(ListView):
    model = Product
    # form_class = ProductForm
    template_name = 'product/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product:index')


class ProductDetailView(DetailView):
    model = Product
    # form_class = ProductForm
    template_name = 'product/detail.html'
    success_url = reverse_lazy('product:index')


class ProductDeleteView(DetailView):
    model = Product
    # form_class = ProductForm
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product:index')


class ProductUpdateView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product:index')


class ProductPriceList(ListView):
    model = Product
    template_name = 'product/product_price.html'
    queryset = Product.custom_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = self.queryset
        return context

    def get_queryset(self):
        return super().get_queryset()


class CategoryList(ListView):
    model = Product
    template_name = 'product/category_list.html'
    context_object_name = 'list'
    # queryset = Product.custom_objects.filter_by_category_name('category')
