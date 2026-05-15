from django.shortcuts import render


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