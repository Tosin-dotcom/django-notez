from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from .models import Category, Note
from .forms import CreateForm, OrderForm, SectorForm


# Create your views here.


def home_view(request):
    return render(request, "home/home_page.html")


""" @login_required(login_url="/user/login")
def story_view(request, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")

    form = OrderForm(request.POST)
    form2 = SectorForm(request.POST)
    if form.is_valid() and form2.is_valid():
        a = form.cleaned_data["order"]
        b = form.cleaned_data["sequence"].strip()
        print(b)
        c = form2.cleaned_data["sec"]
        print(c)
        notes = Note.objects.filter(name=c).order_by(b + a)
        return render(request, "home/story_page.html", {"notes": notes, "form": form, "form2" : form2})

    notes = Note.objects.filter(author=request.user).order_by("-date")
    form = OrderForm()
    form2 = SectorForm()
    return render(
        request,
        "home/story_page.html",
        {
            "notes": notes,
            "form": form,
            "form2" : form2,
        },
    ) """


@login_required(login_url="/user/login")
def story_view(request, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")

    form = OrderForm(request.POST)
    # if request.method == "POST":
    if form.is_valid():
        a = form.cleaned_data["order"]
        b = form.cleaned_data["sequence"].strip()

        notes = Note.objects.filter(author=request.user).order_by(b + a)

    notes = Note.objects.filter(author=request.user).order_by("-date")

    form = OrderForm()
    return render(request, "home/story_page.html", {
        "notes": notes,
        'form': form,
    })


@login_required(login_url="/user/login")
def note_view(request, app, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")
    note = Note.objects.filter(author=request.user).get(title=app)

    return render(request, "home/note_page.html", {"note": note})


@login_required(login_url="/user/login")
def create_view(request, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")
    all_name = Note.objects.filter(
        author=request.user).values_list("title", flat=True)
    all_name = [name.capitalize() for name in all_name]
    form = CreateForm(request.POST)
    if form.is_valid():
        if form.cleaned_data["title"].capitalize() in all_name:
            messages.error(request, "Title already exists")
            form = CreateForm()
        else:
            a = form.cleaned_data["title"]
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(f"/{request.user}/notes/{a}/")

    form = CreateForm()
    return render(request, "home/create_page.html", {"form": form})


@login_required(login_url="/user/login")
def delete_view(request, app, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")
    a = Note.objects.filter(author=request.user).get(title=app)

    if request.method == "POST":
        a.delete()
        return redirect(f"/{request.user}/notes/")

    return render(request, "home/delete_page.html", {})


@login_required(login_url="/user/login")
def edit_view(request, word, user):
    if User.objects.get(username=user) != request.user:
        raise Http404("User does not exists")
    note = Note.objects.filter(author=request.user).get(title=word)

    if request.method == "POST":
        form = CreateForm(request.POST, instance=note)
        if form.is_valid():
            post = form.save(commit=False)
            post.Note = request.user
            post.save()

            return redirect(f"/{request.user}/notes/{form.cleaned_data['title']}/")

    form = CreateForm(instance=note)
    return render(request, "home/edit_page.html", {"note": note, "form": form})
