from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from .forms import SignUpForm, MeForm


class SignUpView(CreateView):
    """ Okno registrace uživatele """
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")


class MeView(LoginRequiredMixin, UpdateView):
    """ Okno uživatele """
    template_name = "form.html"
    model = User
    form_class = MeForm
    success_url = reverse_lazy('accounts:me')

    def get_object(self, pk=None, slug=None, queryset=None):
        """ Vrácení objektu (uživatele) """
        return self.request.user

    def get_initial(self):
        """ Vrácení počátečních dat v okně uživatele (formuláře uživatele) """
        results = super().get_initial()
        results["phone_number"] = self.request.user.profile.personal_phone
        results["email"] = self.request.user.profile.email
        results["address"] = self.request.user.profile.address

        return results


class SubmittableLogoutView(TemplateView):
    """ Okno odhlášení uživatele """
    template_name = 'registration/logout.html'
    # success_url = reverse_lazy("index")
