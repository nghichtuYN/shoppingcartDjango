from django.urls import include, path

urlpatterns = [
    path('products/', include('src.products.urls')),
    path('cart/', include('src.carts.urls')),
    path('', include('src.cartItems.urls')),
]
