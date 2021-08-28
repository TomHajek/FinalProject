from django.db.models import (
    Model, ForeignKey, PositiveIntegerField, DecimalField, CharField,
    DateTimeField, TextField, BooleanField,  # SmallIntegerField,
    SET_NULL,
)

from accounts.models import Profile
from products.models import Product


# from .enums import Status


class Discount(Model):
    """ Sleva produktu """
    name = CharField(max_length=64, null=False, blank=False)
    description = TextField(max_length=128, null=False, blank=False)
    percent = DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    active = BooleanField(default=False, null=True, blank=True)

    discount = ForeignKey(Product, null=True, blank=True, on_delete=SET_NULL)
    # -> discount evidovat k jakému produktu je vázán

    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(null=True, blank=True)
    # deleted_at = DateTimeField(null=False, blank=False)

    def __str__(self):
        return f" {self.name.capitalize()} sleva {self.percent} %."


class Cart(Model):
    """ Nákupní košík """
    user = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    # status = SmallIntegerField(Status.get_choices(), default=10)
    created_at = DateTimeField(auto_now_add=True)
    # session_key = CharField(max_length=40, null=True)

    def __str__(self):
        return f"User no.: {str(self.user_id)}, order no.: {str(self.id)}"

    @property
    def availability(self):
        """ Ověření dostupnosti zboží """
        availability = True
        message = "Zboží je skladem."
        cart_items = self.cartitem_set.all()
        for i in cart_items:
            if i.product.quantity < 0:
                availability = False
                message = "Je nám líto, ale Vámi vybrané zboží není skladem."
        return availability, message

    @property
    def cart_total(self):
        """ Celkem k zaplacení """
        cart_items = self.cartitem_set.all()  # cartitem_set -> self generated "related name"
        total_cost = sum([item.total_cost for item in cart_items])
        return total_cost

    @property
    def cart_items(self):
        """ Počet produktů v košíku """
        cart_items = self.cartitem_set.all()
        total_items = sum([item.quantity for item in cart_items])
        return total_items


class CartItem(Model):
    """ Položky v košíku (Many-To-One relation) """
    cart = ForeignKey(Cart, on_delete=SET_NULL, null=True)  # sem nepřidávat related name
    product = ForeignKey(Product, on_delete=SET_NULL, null=True, blank=False)
    discount = ForeignKey(Discount, on_delete=SET_NULL, related_name="items", null=True)
    quantity = PositiveIntegerField(default=1, null=False, blank=False)
    modified_at = DateTimeField(null=True, blank=True)  # Date added to cart

    class Meta:
        ordering = ["-modified_at"]

    @property
    def total_cost(self):
        if self.discount and self.discount.active:
            discount = self.discount.percent or 1
            total_cost = (self.product.price * discount) * self.quantity
        else:
            total_cost = self.product.price * self.quantity
        return total_cost


class ShippingAddress(Model):
    """ Dodací adresa """
    user = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    address = CharField(max_length=128, null=False, blank=False)
    city = CharField(max_length=128, null=False, blank=False)
    zipcode = CharField(max_length=128, null=False, blank=False)
    state_iso3 = CharField(max_length=3, null=False, blank=False)

    def full_address(self):
        return f"{self.address}, {self.city}, {self.zipcode}, {self.state_iso3},"

    def __str__(self):
        return f"{self.full_address}"


class Order(Model):
    """ Objednávka (faktura) """
    user = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    shipping_address = ForeignKey(ShippingAddress, on_delete=SET_NULL, null=True, blank=True)
    cart_items = ForeignKey(CartItem, on_delete=SET_NULL, related_name="items", null=True)
    total_cost = ForeignKey(Cart, on_delete=SET_NULL, related_name="items", null=True)

    created_at = DateTimeField(auto_now_add=True)

    # status = SmallIntegerField(Status.get_choices())

    def __str__(self):
        return f"Uživatel: {self.user.user_id} {self.user.email} {self.user.phone_number}" \
               f"Dodací adresa: {self.shipping_address.full_address}" \
               f"Položky:{self.cart_items.product} {self.cart_items.quantity}" \
               f"Celkem položek: {self.total_cost.cart_items}" \
               f"Celkem k úhradě: {self.total_cost.cart_total}" \
               f"Datum vytvoření: {self.created_at}" \
             # f"Status: {self.status}"
