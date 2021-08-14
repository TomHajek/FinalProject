from django.shortcuts import render

from .models import Cart, Order


def cart(request):
    context = {
        "cart": Cart.objects.all()
    }
    return render(request, "cart.html", context)


def checkout(request):
    context = {
        "order": Order.objects.all()
    }
    return render(request, "checkout.html", context)
