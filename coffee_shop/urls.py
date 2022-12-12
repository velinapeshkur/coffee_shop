from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from coffee_shop import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    path("access_denied/", views.access_denied, name="access_denied"),
    path("search_coffee/", views.search_coffee, name="search_coffee"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("coffees/", include("coffees.urls", namespace="coffees")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("shop/", include("shop.urls", namespace="checkout")),
    path("coupons/", include("coupons.urls", namespace="coupons")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
