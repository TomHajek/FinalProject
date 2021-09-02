from django.shortcuts import render

from cart.models import Cart
from .models import Product
from .filters import ProductFilter


def products(request):
    """ Okno produktů """
    if request.user.is_anonymous:
        cart_items = 0
    else:
        cart = Cart.objects.filter(user_id=request.user.profile.id).first()
        cart_items = 0
        if cart:
            cart_items = cart.cart_items

    return render(request, "products.html", {
        'filter': ProductFilter(request.GET, queryset=Product.objects.all()),
        'cart_items': cart_items
    })
