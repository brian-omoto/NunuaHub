from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  
from django.http import HttpResponse

# Add a simple home view
def home_view(request):
    return HttpResponse("NunuaHub Store - Welcome to our online store!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),  
    path('orders/', include('orders.urls')),
    path('', home_view, name='home'),
    path('cart/', include('cart.urls', namespace='cart')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)