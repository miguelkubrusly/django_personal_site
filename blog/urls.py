from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.index, name="index"),
    path("posts/<int:post>/", views.redirect_details, name="numeric-details"),
    path("posts/<str:post>/", views.details, name="post-details"),
]
