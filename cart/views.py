import json
from django.shortcuts import render
from django.http import JsonResponse

from cart.models import Cart, CartItem  # Order
from products.models import Product


def cart(request):
    """ Okno košíku """
    if request.user.is_anonymous:
        cart_items = 0
    else:
        cart_obj, _ = Cart.objects.get_or_create(user=request.user.profile)


    return render(request, "cart.html", {
        "cart": cart_obj,
        "cart_items": cart_obj.cart_items
    })


def update_item(request):
    """ Přidání produktů do košíku """
    #if request.user.is_authenticated:
    data = json.loads(request.body)  # request.data
    product_id = data["Product"]
    action = data["Action"]
    print("Action:", action)
    print("Product:", product_id)

    user = request.user.profile
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if action == "add":
        cart_item.quantity += 1
    elif action == "remove":
        cart_item.quantity -= 1

    cart_item.save()

    if cart_item.quantity <= 0:
        cart_item.delete()

    return JsonResponse({"msg": "Item was added", "cnt": cart.cart_items}, safe=False)
"""
    else:
        data = json.loads(request.body)  # request.data
        product_id = data["Product"]
        action = data["Action"]
        print("Action:", action)
        print("Product:", product_id)

        user = None
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=user, session_key=request.session.session_key)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if action == "add":
            cart_item.quantity += 1
        elif action == "remove":
            cart_item.quantity -= 1

        cart_item.save()

        if cart_item.quantity <= 0:
            cart_item.delete()

        return JsonResponse({"msg": "Item was added", "cnt": cart.cart_items}, safe=False)
"""


def checkout(request):
    """ Okno potvrzení objednávky """
    # context = {"cart": Cart.objects.filter(user_id=request.user.id).first()}
    # výsledkem toho bude založený order

    cart_obj, _ = Cart.objects.get_or_create(user=request.user.profile)

    return render(request, "checkout.html", {
        "cart": cart_obj,
        "cart_items": cart_obj.cart_items
    })
