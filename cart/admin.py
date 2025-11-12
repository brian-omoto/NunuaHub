from django.contrib import admin
from .models import ShoppingCart, ShoppingCartItem

@admin.register(ShoppingCart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'total_items', 'created_at']

@admin.register(ShoppingCartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'total_price']

# Register your models here.
