from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "accounts/dashboard.html")
