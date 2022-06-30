from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
]