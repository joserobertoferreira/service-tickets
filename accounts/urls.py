from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import ChangePasswordView, LoginView, RegisterView
from customers.views import search_customer_by_nif

app_name = 'accounts'
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('search_customer/', search_customer_by_nif, name='search_customer'),
]
