from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from shop.models import Order

class HomePage(TemplateView):
    template_name = 'index.html'


def order_complete(request, pk):
    order = Order.objects.get(pk=pk)
    order.complete = True
    order.save()
    return HttpResponse("")

def access_denied(request):
    return render(request, 'access_denied.html')
