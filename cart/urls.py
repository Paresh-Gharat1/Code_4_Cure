from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name = "cart_index"),
    path('covid/', views.covid_home, name = "covid_home"),
    path('diag/', views.diag_home, name = "diag_home"),
]
