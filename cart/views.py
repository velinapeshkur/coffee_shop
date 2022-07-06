from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView


from cart.forms import CartAddProductForm, CartUpdateProductForm
from cart.cart import Cart
from coffees.models import Coffee
from coupons.forms import CouponApplyForm

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        print(cd['from_template'])

        if cd['from_template'] == 'coffee_detail':
            return redirect('coffees:coffee_detail', pk=product.pk)
        elif cd['from_template'] == 'coffee_list':
            return redirect('coffees:all_coffees')
        else:
            return redirect('coffees:coffees_by_category', pk=int(cd['from_template'][-1]))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    form = CartAddProductForm
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'quantity_form': form})


def update_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=True)
    return redirect('cart:cart_detail')
