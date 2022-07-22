from django.urls import path
from . import views

app_name = 'coffees'

urlpatterns = [
    path('', views.CoffeeListView.as_view(), name='all_coffees'),
    path('<int:pk>/', views.list_by_category, name='coffees_by_category'),
    path('coffee/<int:pk>/', views.CoffeeDetailView.as_view(), name='coffee_detail'),
]
