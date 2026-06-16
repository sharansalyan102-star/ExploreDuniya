from django.urls import path
from .views import (
    home,
    place_list,
    place_detail,
    category_places,
    register,
    suggest_place,
)

urlpatterns = [
    path("", home, name="home"),

    path("register/", register, name="register"),

    path("places/", place_list, name="place_list"),

    path(
        "places/category/<str:category>/",
        category_places,
        name="category_places",
    ),

    path(
        "places/<int:place_id>/",
        place_detail,
        name="place_detail",
    ),

    path(
        "suggest-place/",
        suggest_place,
        name="suggest_place",
    ),
]