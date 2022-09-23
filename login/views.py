from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["Username"].title()
            password = form.cleaned_data["Password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(f"/{user}/notes/")
            else:
                messages.error(request, "Username or password is incorrect")

    form = LoginForm()
    return render(
        request,
        "login/home.html",
        {
            "form": form,
        },
    )


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["Username"].title()
            email = form.cleaned_data["Email"].lower()
            p1 = form.cleaned_data["Password1"]
            p2 = form.cleaned_data["Password2"]

            users = User.objects.values_list("username", flat=True)

            if username in users:
                messages.error(request, "Username already exists")
            else:
                if p1 == p2:
                    user = User.objects.create_user(
                        username=username, password=p1, email=email)
                    user.save()
                    login(request, user)
                    return redirect(f"/{user.username}/notes/")
                else:
                    messages.error(request, "Passwords don't match")

    form = RegisterForm()
    return render(request, "login/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
