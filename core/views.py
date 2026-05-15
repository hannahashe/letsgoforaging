from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import BlogPost, Event, GalleryImage, Review


def site_context():
    """Return shared context used across simple site pages."""
    return {
        "current_year": date.today().year,
    }


def home(request):
    """Display the website homepage with featured content."""
    featured_event = Event.objects.filter(
        is_published=True,
        is_featured=True,
    ).first()

    featured_post = BlogPost.objects.filter(
        is_published=True,
        is_featured=True,
    ).first()

    featured_images = GalleryImage.objects.filter(
        is_published=True,
        is_featured=True,
    )[:3]

    featured_reviews = Review.objects.filter(
        is_published=True,
        is_featured=True,
    )[:3]

    context = {
        **site_context(),
        "featured_event": featured_event,
        "featured_post": featured_post,
        "featured_images": featured_images,
        "featured_reviews": featured_reviews,
    }

    return render(request, "core/home.html", context)


def about(request):
    """Display the about page."""
    return render(request, "core/about.html", site_context())


def contact(request):
    """Display the contact page."""
    return render(request, "core/contact.html", site_context())


def gallery(request):
    """Display published gallery images."""
    images = GalleryImage.objects.filter(is_published=True)

    return render(
        request,
        "core/gallery.html",
        {
            **site_context(),
            "images": images},
    )


def event_list(request):
    """Display published upcoming foraging events."""
    events = Event.objects.filter(is_published=True)

    return render(
        request,
        "core/event_list.html",
        {
            **site_context(),
            "events": events
        },
    )


def event_detail(request, slug):
    """Display a single published foraging event."""
    event = get_object_or_404(Event, slug=slug, is_published=True)

    return render(
        request,
        "core/event_detail.html",
        {
            **site_context(),
            "event": event
        },
    )


def blog_list(request):
    """Display published blog posts."""
    posts = BlogPost.objects.filter(is_published=True)

    return render(
        request,
        "core/blog_list.html",
        {
            **site_context(),
            "posts": posts
        },
    )


def blog_detail(request, slug):
    """Display a single published blog post."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    return render(
        request,
        "core/blog_detail.html",
        {
            **site_context(),
            "post": post
        },
    )
