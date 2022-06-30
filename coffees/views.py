from unicodedata import category
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from coffees.models import Coffee, Categories
from cart.forms import CartAddProductForm

# Create your views here.

class CoffeeDetailView(DetailView):
    model = Coffee
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_add_form'] = CartAddProductForm()
        return context
    

class CoffeeListView(ListView):
    model = Coffee

    def get_queryset(self):
        return Coffee.objects.all()

   
def list_by_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'coffees/coffee_list.html', {'coffee_list': Coffee.objects.filter(category=category),
                                                        'category_name': category.category_name})
