from django import forms
from django_countries.widgets import CountrySelectWidget
from shop.models import ShippingAddress, Order


class ContactInfoForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email')


class ShippingAddressForm(forms.ModelForm):
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address (Street, Building, etc.)'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}))
    postal_code = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Postal Code'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}))
    
    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'postal_code', 'state', 'country')
        
        widgets = {'country': CountrySelectWidget(layout='{widget}', attrs={'class':'form-control'})}

        
class PaymentMethodForm(forms.Form):
    PaymentChoices = (
        ('Online', 'Pay Online'),
        ('COD', 'Pay on delivery'),
    )
    
    payment = forms.ChoiceField(label="", choices=PaymentChoices, widget=forms.RadioSelect)
