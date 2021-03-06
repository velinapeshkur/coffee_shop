from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create_order/', views.create_order, name='create_order'),
    path('payment/<int:pk>/', views.payment_view, name='payment'),
    path('paid/<int:pk>/', views.paid, name='paid'),
    path('order_confirmation/<int:pk>/', views.confirm_order, name='confirm_order'),
    path('order_history/', views.OrderListView.as_view(), name='order_history'),
]
