from django.shortcuts import render


def home(request):
    """Display the website homepage."""
    return render(request, "core/home.html")