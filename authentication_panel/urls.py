from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name = "authentication_panel/login.html"), name = "login"),
	path('logout/', auth_views.LogoutView.as_view(template_name = "authentication_panel/logout.html"), name = "logout"),
    path('register/', views.register, name = "register"),
]
