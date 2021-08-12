from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.forms import (
    CharField, ModelChoiceField, EmailField,
)

from .models import Profile, Address


class SignUpForm(UserCreationForm):
    """ Formulář - registrace uživatele """
    class Meta(UserCreationForm.Meta):
        fields = [
            "username",
            "first_name",
            "last_name",
        ]

    phone_number = CharField(max_length=32, required=False)
    email = EmailField(max_length=128, required=True)

    @atomic
    def save(self, commit=True):
        """ Uložení dat do databáze """
        # --- Vložení do auth_user ...
        result = super().save(commit)

        profile = Profile(
            user=result,
            phone_number=self.cleaned_data["phone_number"],
            email=self.cleaned_data["email"],
        )

        if commit:
            # --- Vložení do accounts_profile ...
            profile.save()

        return result


class MeForm(UserChangeForm):
    """ Formulář - přehled uživatele (update osobních informací)"""
    class Meta(UserChangeForm.Meta):
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

    phone_number = CharField(max_length=32, required=False)
    email = EmailField(max_length=128, required=True)
    address = ModelChoiceField(
        queryset=Address.objects,
        required=False
    )

    @atomic
    def save(self, commit=True):
        """ Uložení dat do databáze (update) """
        result: User = super().save(commit)

        result.profile.phone_number = self.cleaned_data["phone_number"]
        result.profile.email = self.cleaned_data["email"]
        result.profile.address = self.cleaned_data["address"]

        if commit:
            result.profile.save()

        return result
