from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create-test/', views.create_test_order, name='create_test_order'),
    path('<str:order_number>/', views.order_detail, name='order_detail'),
]