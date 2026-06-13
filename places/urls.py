from django.urls import path
from .views import (
    home,
    place_list,
    place_detail,
    category_places
)

urlpatterns = [
    path('', home),

    path('places/', place_list),

    path(
        'places/category/<str:category>/',
        category_places
    ),

    path(
        'places/<int:place_id>/',
        place_detail
    ),
    path(
    "places/<int:place_id>/",
    place_detail,
    name="place_detail",
),
]