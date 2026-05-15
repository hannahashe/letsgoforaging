from django.db import models
from django.urls import reverse


class Event(models.Model):
    """A foraging walk or event listed on the website."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    meeting_point = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ticket_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})


class BlogPost(models.Model):
    """A blog post or article for the Field Notes section."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.CharField(max_length=255)
    body = models.TextField()
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})


class GalleryImage(models.Model):
    """An image displayed in the website gallery."""

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/")
    alt_text = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Review(models.Model):
    """A customer review or testimonial."""

    reviewer_name = models.CharField(max_length=100)
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    source = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional: where the review came from, e.g. Google, Facebook, Eventbrite.",
    )
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating} stars"
