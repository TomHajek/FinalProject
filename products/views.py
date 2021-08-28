from django.shortcuts import render

from .models import Product
from .filters import ProductFilter
from cart.models import Cart


def products(request):
    """ Okno produktů """
    # cart_items = Cart.objects.filter(user_id=request.user.id).first().cart_items
    cart_items = Cart.cart_items
    products = Product.objects.all()

    #context = {"products": products, "cart_items": cart_items}
    #return render(request, "products.html", context)

    context = {}
    filtered_products = ProductFilter(
        request.GET,
        queryset=Product.objects.all()
    )

    context["filtered_products"] = filtered_products
    return render(request, "products.html", context)
