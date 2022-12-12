from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm, CartUpdateProductForm
from coffees.models import Coffee


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart.add(
            product=product,
            quantity=data.get("quantity"),
            update_quantity=data.get("update"),
        )

        # Reloads current page
        match data.get("from_template"):
            case "coffee_detail":
                return redirect("coffees:coffee_detail", pk=product.pk)
            case "coffee_list":
                return redirect("coffees:all_coffees")
            case _:
                return redirect(
                    "coffees:coffees_by_category", pk=int(data["from_template"][-1])
                )


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail_view(request):
    cart = Cart(request)
    form = CartAddProductForm
    return render(
        request, "cart/cart_detail.html", {"cart": cart, "quantity_form": form}
    )


def update_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Coffee, id=product_id)
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add(product=product, quantity=data.get("quantity"), update_quantity=True)
    return redirect("cart:cart_detail")
