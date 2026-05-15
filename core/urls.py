from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("walks/", views.event_list, name="event_list"),
    path("walks/<slug:slug>/", views.event_detail, name="event_detail"),
    path("field-notes/", views.blog_list, name="blog_list"),
    path("field-notes/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
]
