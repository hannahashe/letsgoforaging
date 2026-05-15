from django.contrib import admin
from .models import BlogPost, Event, GalleryImage, Review


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
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Main event details",
            {
                "fields": (
                    "title",
                    "slug",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Date, time and location",
            {
                "fields": (
                    "date",
                    "start_time",
                    "end_time",
                    "location",
                    "meeting_point",
                )
            },
        ),
        (
            "Booking information",
            {
                "fields": (
                    "price",
                    "ticket_url",
                )
            },
        ),
        (
            "Publishing options",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


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
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Article content",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "body",
                )
            },
        ),
        (
            "Publishing options",
            {
                "fields": (
                    "published_date",
                    "is_published",
                    "is_featured",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Admin settings for gallery images."""

    list_display = (
        "title",
        "is_published",
        "is_featured",
        "created_at",
    )
    list_filter = ("is_published", "is_featured", "created_at")
    search_fields = ("title", "alt_text", "caption")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        (
            "Image details",
            {
                "fields": (
                    "title",
                    "image",
                    "alt_text",
                    "caption",
                )
            },
        ),
        (
            "Publishing options",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin settings for customer reviews."""

    list_display = (
        "reviewer_name",
        "rating",
        "source",
        "is_published",
        "is_featured",
        "created_at",
    )
    list_filter = ("rating", "source", "is_published", "is_featured")
    search_fields = ("reviewer_name", "quote", "source")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        (
            "Review content",
            {
                "fields": (
                    "reviewer_name",
                    "quote",
                    "rating",
                    "source",
                )
            },
        ),
        (
            "Publishing options",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )