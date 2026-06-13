from django.shortcuts import render, get_object_or_404
from .models import Place, Review

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


from django.shortcuts import render, get_object_or_404, redirect

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    if request.method == "POST":
        user_name = request.POST.get("user_name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            place=place,
            user_name=user_name,
            rating=rating,
            comment=comment
        )

        return redirect("place_detail", place_id=place.id)

    return render(
        request,
        "places/place_detail.html",
        {
            "place": place,
        },
    )
def home(request):
    places = Place.objects.all()[:3]

    return render(
        request,
        'places/home.html',
        {'places': places}
    )
def category_places(request, category):

    places = Place.objects.filter(
        category=category
    )

    return render(
        request,
        'places/place_list.html',
        {'places': places}
    )
def category_places(request, category):

    places = Place.objects.filter(
        category=category
    )

    return render(
    request,
    'places/place_list.html',
    {
        'places': places,
        'category': category
    }
)
    