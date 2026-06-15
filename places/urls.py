from django.urls import path
from .views import (
    home,
    place_list,
    place_detail,
    category_places,
    register,
)

urlpatterns = [
    # Home
    path("", home, name="home"),

    # User Registration
    path("register/", register, name="register"),

    # Places
    path("places/", place_list, name="place_list"),

    # Category Filter
    path(
        "places/category/<str:category>/",
        category_places,
        name="category_places",
    ),

    # Place Detail
    path(
        "places/<int:place_id>/",
        place_detail,
        name="place_detail",
    ),
]