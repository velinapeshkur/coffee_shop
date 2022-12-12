from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
    path("checkout/", views.checkout_view, name="checkout"),
    path("create_order/", views.create_order_view, name="create_order"),
    path("payment/<int:pk>/", views.payment_view, name="payment"),
    path("paid/<int:pk>/", views.mark_order_as_paid_view, name="paid"),
    path("confirm_order/<int:pk>/", views.confirm_order_view, name="confirm_order"),
    path("my_orders/", views.OrderListView.as_view(), name="order_history"),
]
