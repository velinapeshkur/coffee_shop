from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import forms, models
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
import avinit


# Create your views here.

# Generate user avatar
def get_avatar(request, user):
    avatar_colors = ['#F8BB05',]
    avatar_options = {"width": "42",
                      "height": "42",
                      "radius": "21",
                      "font-size": "15",
                      "font-weight": "bold"}
    large_avatar_options = {"width": "120",
                            "height": "120",
                            "radius": "60",
                            "font-size": "45",
                            "font-weight": "bold"}
    request.session['avatar'] = avinit.get_svg_avatar(user.get_full_name(), 
                                                      colors=avatar_colors, 
                                                      **avatar_options)
    request.session['large_avatar'] = avinit.get_svg_avatar(user.get_full_name(),
                                                            colors=avatar_colors,
                                                            **large_avatar_options)


def logout_check(user):
    return user.is_anonymous


@user_passes_test(logout_check, login_url='/access_denied/')
def sign_up(request):
    form = forms.ProfileCreateForm()
    
    if request.method == "POST":
        form = forms.ProfileCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            get_avatar(request=request, user=user)
            return redirect('home')
        
    return render(request, 'accounts/signup.html', {'form': form})


@user_passes_test(logout_check, login_url='/access_denied/')
def login_view(request):    
    form = forms.CustomAuthForm()
    
    if request.method == 'POST':
        form = forms.CustomAuthForm(request=request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            checkout_login = form.cleaned_data.get('checkout_login')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                get_avatar(request=request, user=user)

                if checkout_login:
                    return redirect('shop:checkout')
                return redirect('home')
        
    return render(request, "accounts/login.html", {"form": form})


class UpdateProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    template_name = 'accounts/profile_update.html'
    form_class = forms.ProfileUpdateForm
    
    # Checks if user is accessing their own profile page
    def test_func(self):
        return self.kwargs['pk'] == self.request.user.pk

    def handle_no_permission(self):
        return redirect('access_denied')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        get_avatar(request=request, user=self.object)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_form'] = forms.PasswordUpdateForm(user=self.get_object())
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Your profile information is successfully updated")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        error_list = ''
        for field, error in form.errors.items():
            error_list += error
        messages.error(self.request, error_list)
        return super().form_invalid(form)

class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = models.CustomUser
    success_url = reverse_lazy('home')
    
    def get(self, *args, **kwargs):
        return redirect('access_denied')


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/profile_update.html'
    
    def get(self, *args, **kwargs):
        return redirect('access_denied')
    
    def get_success_url(self):  
        return reverse_lazy('accounts:update', kwargs = {'pk': self.request.user.pk})       
    
    def form_valid(self, form):
        messages.success(self.request, "Your password is successfully changed")
        return super().form_valid(form)

    def form_invalid(self, form):
        error_list = ''
        for field, error in form.errors.items():
            error_list += error
        messages.error(self.request, error_list)
        return HttpResponseRedirect(self.get_success_url())
