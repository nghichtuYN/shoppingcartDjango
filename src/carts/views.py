from django.shortcuts import render
from src.carts.models import Cart

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id) if cart_id else None
    return render(request, 'cart_detail.html', {'cart': cart})
