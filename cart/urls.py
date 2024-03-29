from django.urls import path
from .views import cart, checkout, update_item

app_name = "cart"
urlpatterns = [
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("cart/update_item/", update_item, name="update_item")
]
