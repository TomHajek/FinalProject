from django.contrib import admin

from .models import Discount, Cart, CartItem, ShippingAddress


admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
