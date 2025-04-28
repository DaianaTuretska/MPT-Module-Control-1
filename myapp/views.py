# myapp/views.py
from django.shortcuts import render

from .models import Product


def home(request):
    # pull all products from the ORM
    products = Product.objects.all()
    return render(request, "myapp/home.html", {"products": products})
