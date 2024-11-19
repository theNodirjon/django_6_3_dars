from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # "/" manzil uchun view
    path('users/', views.users, name='users'),  # "/users" manzil uchun view
    path('ads/', views.ads, name='ads'),  # "/ads" manzil uchun view
]
