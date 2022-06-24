from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from accounts.models import User


class ProfileCreateForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    class Meta:
        model = User
        
        
class ProfileUpdateForm(UserChangeForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
  
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
