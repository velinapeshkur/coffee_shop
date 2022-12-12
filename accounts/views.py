from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from accounts import forms, services
from accounts.models import User


@user_passes_test(services.logout_check, login_url="/access_denied/")
def signup_view(request):
    form = forms.ProfileCreateForm()

    if request.method == "POST":
        form = forms.ProfileCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            services.get_user_avatar(request, full_name=user.get_full_name())
            return redirect("home")

    return render(request, "accounts/signup.html", {"form": form})


@user_passes_test(services.logout_check, login_url="/access_denied/")
def login_view(request):
    form = forms.CustomAuthForm()

    if request.method == "POST":
        form = forms.CustomAuthForm(request=request, data=request.POST)

        if form.is_valid():
            login_data = form.cleaned_data
            services.user_login(login_data)

            checkout_login = login_data.get(
                "checkout_login"
            )  # Checks if user was logged in from checkout page
            if checkout_login:
                return redirect("shop:checkout")

            return redirect("home")

    return render(request, "accounts/login.html", {"form": form})


class UpdateProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "accounts/profile_update.html"
    form_class = forms.ProfileUpdateForm

    def test_func(self):
        """
        Checks if user is accessing their own page.
        Test function for UserPassesTestMixin.
        """
        return self.kwargs["pk"] == self.request.user.pk

    def handle_no_permission(self):
        return redirect("access_denied")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        services.get_user_avatar(request=request, full_name=self.object.get_full_name())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_form"] = forms.PasswordUpdateForm(user=self.get_object())
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Your profile information is successfully updated"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        error_list = ""
        for field, error in form.errors.items():
            error_list += error
        messages.error(self.request, error_list)
        return super().form_invalid(form)


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("home")

    def get(self, *args, **kwargs):
        return redirect("access_denied")


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/profile_update.html"

    def get(self, *args, **kwargs):
        return redirect("access_denied")

    def get_success_url(self):
        return reverse_lazy("accounts:update", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        messages.success(self.request, "Your password is successfully changed")
        return super().form_valid(form)

    def form_invalid(self, form):
        error_list = ""
        for field, error in form.errors.items():
            error_list += error
        messages.error(self.request, error_list)
        return HttpResponseRedirect(self.get_success_url())
