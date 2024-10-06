from django.shortcuts import render
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def product_list(request):
    products = Product.objects.all()
    if not products.exists():
        return render(request, 'product_list.html', {'products': [], 'total_value': 0})

    total_value = sum([p.price * p.quantity for p in products]) # Change cost by price to match the model
    return render(request, 'product_list.html', {'products': products, 'total_value': total_value})