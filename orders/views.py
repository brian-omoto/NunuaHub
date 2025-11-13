from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from store.models import Product

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def create_test_order(request):
    """Create a test order manually for development"""
    # Get some products to add to the order
    products = Product.objects.all()[:2]  # Get first 2 available products
    
    if not products:
        messages.error(request, "No products available. Please add products first.")
        return redirect('store:product_list')
    
    # Calculate total amount
    total_amount = sum(product.price for product in products)
    
    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        shipping_address="123 Test Street, Nairobi, Kenya",
        billing_address="123 Test Street, Nairobi, Kenya",
        status='processing'
    )
    
    # Add order items
    for product in products:
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            price=product.price
        )
    
    messages.success(request, f"Test order #{order.order_number} created successfully!")
    return redirect('orders:order_detail', order_number=order.order_number)