from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been successfully created! Login to continue {username}')
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, "authentication_panel/register.html", {"form" : form})