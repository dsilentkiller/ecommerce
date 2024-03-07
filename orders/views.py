from django.shortcuts import render
from orders.models import *
from django.views.generic import ListView
# , DetailView, CreateView
# Create your views here.


class OrderListView(ListView):
    model = OrderItem

