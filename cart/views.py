from django.shortcuts import render

from .models import Cart  # Order


def cart(request):
    """ Okno košíku """
    context = {
        "cart": Cart.objects.filter(user_id=request.user.id).first()
    }
    return render(request, "cart.html", context)


def checkout(request):
    """ Okno potvrzení objednávky """
    context = {
        "cart": Cart.objects.filter(user_id=request.user.id).first()
    }
    # výsledkem toho bude založený order

    return render(request, "checkout.html", context)
