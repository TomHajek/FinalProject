"""
Nastavení cest pro zobrazení oken registrace uživatelů:
   - registrace
   - přehled (informace uživatele)
   - přihlášení
   - odhlášení
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignUpView, MeView, SubmittableLogoutView

app_name = "accounts"
urlpatterns = [
   path("signup/", SignUpView.as_view(), name="sign_up"),
   path("me/", MeView.as_view(), name="me"),

   path("login/", LoginView.as_view(), name="log_in"),
   path("logout/", LogoutView.as_view(), name="log_out"),

   path("logout/request/", SubmittableLogoutView.as_view(), name="logout_request"),
]
