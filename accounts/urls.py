from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('<int:pk>/update/', views.UpdateProfileView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteProfileView.as_view(), name='delete'),
    path('<int:pk>/password/', views.UpdatePassword.as_view(), name='password_change'),
]
