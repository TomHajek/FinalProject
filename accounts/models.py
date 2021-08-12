from django.contrib.auth.models import User
from django.db.models import (
    Model,  CharField, OneToOneField, EmailField, ForeignKey,
    CASCADE, PROTECT
)


class Address(Model):
    """ Adresa uživatele """
    address = CharField(max_length=128, null=False, blank=False)
    city = CharField(max_length=128, null=False, blank=False)
    zipcode = CharField(max_length=128, null=False, blank=False)
    state_iso3 = CharField(max_length=3, null=False, blank=False)

    def full_address(self):
        return f"{self.address}, {self.city}, {self.zipcode}, {self.state_iso3},"

    def __str__(self):
        return f"{self.full_address}"


class Profile(Model):
    """ Uživatelský profil """
    user = OneToOneField(User, on_delete=CASCADE)
    phone_number = CharField(
        max_length=16,
        default="",
        blank=True,
        null=False,
    )
    email = EmailField(
        max_length=128,
        default='',
        blank=False,
        null=False
    )
    address = ForeignKey(
        Address,
        on_delete=PROTECT,
        blank=True,
        null=True
    )

    def __str__(self):
        return f" {self.user_id} {self.email}"
