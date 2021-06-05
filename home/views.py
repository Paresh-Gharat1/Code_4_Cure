from django.shortcuts import render
from .models import Feedback
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email_user = request.POST.get("email")
        number = request.POST.get("number")
        text = request.POST.get("text")
        obj = Feedback(name = full_name, email = email_user, mobile_number = number, message = text)
        obj.save()
    return render(request, "home/homepage.html")