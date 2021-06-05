from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def cart_home(request):
	return render(request, "cart/index.html")

@login_required
def covid_home(request):
	return render(request, "cart/covid.html")

@login_required
def diag_home(request):
	return render(request, "cart/diag.html")