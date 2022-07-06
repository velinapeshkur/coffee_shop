from email.policy import default
from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="")
    from_template = forms.CharField(max_length=256, required=False, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartUpdateProductForm(forms.Form):
    quantity = forms.IntegerField(label="")
