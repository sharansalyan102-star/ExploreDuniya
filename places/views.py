from django.shortcuts import render, get_object_or_404
from .models import Place


def place_list(request):
    places = Place.objects.all()

    return render(
        request,
        'places/place_list.html',
        {'places': places}
    )


def place_detail(request, place_id):
    place = get_object_or_404(
        Place,
        id=place_id
    )

    return render(
        request,
        'places/place_detail.html',
        {'place': place}
    )
def home(request):
    return render(
        request,
        'places/home.html'
    )
    