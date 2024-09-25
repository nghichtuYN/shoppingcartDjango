from django.shortcuts import get_object_or_404, redirect,render
from .models import CartItem
from src.carts.models import Cart
from src.products.models import Product
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
    if created:
        cart_item.quantity = 1  
    else:
        cart_item.quantity += 1 
    cart_item.save()
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'cart': cart})

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()  
        cart_item.save()
    
    return redirect('cart_detail')  

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    
    return redirect('cart_detail')  