from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Cart, CartItem

def store_home(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'store/category_products.html', {
        'category': category,
        'products': products
    })