from django.contrib.auth.models import User
from django.db.models import (
    Model, OneToOneField, CharField, EmailField, TextField,
    CASCADE,
)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(null=True, blank=True)

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
