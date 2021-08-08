from django.contrib.auth.models import User
from django.db.models import (
    Model, OneToOneField, CharField, EmailField,
    CASCADE,
)


class Profile(Model):
    """ Uživatelské profily """
    user = OneToOneField(User, on_delete=CASCADE)
    username = CharField(max_length=64, null=False)
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

    def __str__(self):
        return f" {self.user_id} {self.username} {self.email}"
