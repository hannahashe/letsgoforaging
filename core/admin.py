from django.contrib import admin
from .models import Event


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