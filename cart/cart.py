from decimal import Decimal

from django.conf import settings

from coffees.models import Coffee
from coupons.models import Coupon


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Coffee.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            if not item["product"].out_of_stock():
                item["price"] = Decimal(item["price"])
                item["total_price"] = item["price"] * item["quantity"]
            else:
                item["price"] = 0
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Adds item to cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        """
        Saves updated cart in session.
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        Removes product from cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """
        Calculates total price for all items in cart.
        """
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def get_coupon_price(self):
        """
        Recalculates total cart price after coupon is applied.
        """
        coupon_id = self.session.get("coupon_id")
        coupon = Coupon.objects.get(id=coupon_id)
        discount = coupon.discount
        return self.get_total_price() - (self.get_total_price() * discount / 100)

    def clear(self):
        """
        Clears cart.
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
