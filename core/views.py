from django.shortcuts import get_object_or_404, render
from .models import BlogPost, Event, GalleryImage



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
    """Display published gallery images."""
    images = GalleryImage.objects.filter(is_published=True)

    return render(
        request,
        "core/gallery.html",
        {"images": images},
    )


def event_list(request):
    """Display published upcoming foraging events."""
    events = Event.objects.filter(is_published=True)

    return render(
        request,
        "core/event_list.html",
        {"events": events},
    )


def event_detail(request, slug):
    """Display a single published foraging event."""
    event = get_object_or_404(Event, slug=slug, is_published=True)

    return render(
        request,
        "core/event_detail.html",
        {"event": event},
    )


def blog_list(request):
    """Display published blog posts."""
    posts = BlogPost.objects.filter(is_published=True)

    return render(
        request,
        "core/blog_list.html",
        {"posts": posts},
    )


def blog_detail(request, slug):
    """Display a single published blog post."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    return render(
        request,
        "core/blog_detail.html",
        {"post": post},
    )
