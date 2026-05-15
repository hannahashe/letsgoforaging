from django.shortcuts import render
from .models import Event


def home(request):
    """Display the website homepage."""
    return render(request, "core/home.html")


def about(request):
    """Display the about page."""
    return render(request, "core/about.html")


def contact(request):
    """Display the contact page."""
    return render(request, "core/contact.html")


def gallery(request):
    """Display the gallery page."""
    return render(request, "core/gallery.html")


def event_list(request):
    """Display published upcoming foraging events."""
    events = Event.objects.filter(is_published=True)

    return render(
        request,
        "core/event_list.html",
        {"events": events},
    )