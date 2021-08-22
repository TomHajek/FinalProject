from django.shortcuts import render

from .models import Product
from cart.models import Cart


def products(request):
    """ Okno produktů """
    cart_items = Cart.cart_items
    products = Product.objects.all()

    context = {"products": products, "cart_items": cart_items}
    return render(request, "products.html", context)
