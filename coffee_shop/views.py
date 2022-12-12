from django.shortcuts import render
from django.views.generic import TemplateView

from coffees.models import Coffee


class HomePage(TemplateView):
    template_name = "index.html"


def access_denied(request):
    return render(request, "access_denied.html")


def search_coffee(request):
    search_text = request.POST.get("search")
    results = Coffee.objects.filter(name__icontains=search_text)
    return render(
        request, "search_results.html", {"results": results, "search_text": search_text}
    )
