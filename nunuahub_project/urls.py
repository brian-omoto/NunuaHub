from django.contrib import admin
from django.urls import path, include  # Fixed: 'urls' not 'url'
from django.http import HttpResponse

# Add a simple home view
def home_view(request):
    return HttpResponse("NunuaHub Store - Welcome to our online store!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),  
    path('', home_view, name='home'),
    path('cart/', include('cart.urls', namespace='cart')),

]