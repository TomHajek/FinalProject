from django.shortcuts import render

from .models import Cart, Order


def cart(request):
    """ Okno košíku """
    context = {
        "cart": Cart.objects.all()
    }
    return render(request, "cart.html", context)


def checkout(request):
    """ Okno potvrzení objednávky """
    context = {
        "order": Order.objects.all()
    }
    return render(request, "checkout.html", context)
