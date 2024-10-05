from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    total_value = sum([p.cost * p.quantity for p in products])
    return render(request, 'product_list.html', {'products': products, 'total_value': total_value})