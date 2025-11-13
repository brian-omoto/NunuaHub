from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField(default='Address not provided')
    billing_address = models.TextField(default='Address not provided')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return f"Order #{self.order_number} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            import datetime
            date_str = datetime.datetime.now().strftime('%Y%m%d')
            last_order = Order.objects.filter(order_number__startswith=f'ORD{date_str}').order_by('-order_number').first()
            if last_order:
                last_num = int(last_order.order_number[-4:])
                new_num = last_num + 1
            else:
                new_num = 1
            self.order_number = f"ORD{date_str}{new_num:04d}"
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return f"{self.quantity} x {self.product.name}"
    
    def total_price(self):
        return self.quantity * self.price

