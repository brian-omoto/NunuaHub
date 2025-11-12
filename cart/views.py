from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  ShoppingCart, ShoppingCartItem
from store.models import Product

@login_required
def cart_detail(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    cart_item, created = ShoppingCartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:cart_detail')
# Create your views here.
