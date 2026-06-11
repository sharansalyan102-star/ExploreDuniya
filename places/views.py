from django.shortcuts import render, get_object_or_404
from .models import Place, FoodSpot, Stay, Review

def place_list(request):

    query = request.GET.get('q')

    if query:
        places = Place.objects.filter(
            name__icontains=query
        )
    else:
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
    places = Place.objects.all()[:3]

    return render(
        request,
        'places/home.html',
        {'places': places}
    )
    