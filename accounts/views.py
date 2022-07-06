from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, View
from requests import request

from cart.cart import Cart
from . import forms, models
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
import avinit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User as auth_User
import copy
from django.contrib.auth import logout



# Create your views here.

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


# def logout_view(request):
#     cart = copy.deepcopy(Cart(request).cart)
#     logout(request)
#     session = request.session
#     session[settings.CART_SESSION_ID] = cart
#     session.modified = True
    
#     return redirect('home')


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    template_name = 'accounts/profile_update.html'
    form_class = forms.ProfileUpdateForm
    
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


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/profile_update.html'
    
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


# class UpdateAddress(LoginRequiredMixin, View):
#     template_name = 'accounts/profile_update.html'
    
#     def get_success_url(self):  
#         return reverse_lazy('accounts:update', kwargs = {'pk': self.request.user.pk})
    
#     def post(self, request, *args, **kwargs):

#         user = get_object_or_404(models.User, pk=self.request.user.pk)
#         form = forms.AddressUpdateForm(data=request.POST)

#         if form.is_valid():
#             address = form.save(commit=False)
#             address.customer = user
#             address.save()
#             user.address = address
#             user.save()
#             messages.success(request, "Your shipping address is successfully updated")
#             return HttpResponseRedirect(self.get_success_url())
        
#         else:
#             error_list = ''
#             for field, error in form.errors.items():
#                 error_list += error
#             messages.error(request, error_list)
#             return HttpResponseRedirect(self.get_success_url())
    