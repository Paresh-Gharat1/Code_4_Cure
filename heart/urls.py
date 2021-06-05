from django.urls import path
from . import views

urlpatterns = [
    path('', views.check, name = "check"),
    path("consult/", views.consult, name = "consult"),
]
