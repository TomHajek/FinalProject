import json
from django.shortcuts import render
from django.http import JsonResponse

from cart.models import Cart, CartItem  # Order
from products.models import Product


def cart(request):
    """ Okno košíku """
    context = {
        "cart": Cart.objects.filter(user_id=request.user.id).first()
    }

    # data = update_item(request)
    # cart_items = data["cart_items"]
    # cart = data["cart"]
    # items = data["items"]
    # context = {"items": items, "cart": cart, "cart_items": cart_items}

    return render(request, "cart.html", context)


def checkout(request):
    """ Okno potvrzení objednávky """
    context = {
        "cart": Cart.objects.filter(user_id=request.user.id).first()
    }
    # výsledkem toho bude založený order

    return render(request, "checkout.html", context)


def update_item(request):
    data = json.loads(request.body)  # request.data
    product_id = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("Product:", product_id)

    user = request.user.profile
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if action == "add":
        cart_item.quantity = (cart_item.quantity + 1)
    elif action == "remove":
        cart_item.quantity = (cart_item.quantity - 1)

    cart_item.save()

    if cart_item.quantity <= 0:
        cart_item.delete()

    return JsonResponse("Item was added", safe=False)
