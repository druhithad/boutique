# cart/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from shop.models import Product

@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.total_price() for item in cart_items)
    
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass  # You can also add a message if needed

    return redirect('cart:cart_detail')

