from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home,name='home'),
    path('customer/<str:pk>/',views.customer,name='customer'),
]