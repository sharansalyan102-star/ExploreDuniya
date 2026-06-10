from django.urls import path
from .views import home, place_list, place_detail

urlpatterns = [
    path('', home),
    path('places/', place_list),
    path('places/<int:place_id>/', place_detail),
]