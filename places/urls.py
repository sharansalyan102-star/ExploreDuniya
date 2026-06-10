from django.urls import path
from .views import place_list, place_detail

urlpatterns = [
    path('', place_list),
    path('<int:place_id>/', place_detail),
]