from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

"""
MAIN PRODUCTS PAGE
"""
@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})