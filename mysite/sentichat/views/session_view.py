from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            error_msg = "Invalid login credentials"
            return render(request, "login.html", {"error_message": error_msg})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
