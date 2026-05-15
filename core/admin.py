from django.contrib import admin
from .models import BlogPost, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin settings for foraging events."""

    list_display = (
        "title",
        "date",
        "start_time",
        "location",
        "is_published",
        "is_featured",
    )
    list_filter = ("is_published", "is_featured", "date")
    search_fields = ("title", "short_description", "description", "location")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("date", "start_time")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin settings for blog posts and articles."""

    list_display = (
        "title",
        "published_date",
        "is_published",
        "is_featured",
    )
    list_filter = ("is_published", "is_featured", "published_date")
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-published_date",)