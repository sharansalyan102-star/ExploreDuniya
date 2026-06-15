from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Place, Review


# -------------------------
# Home Page
# -------------------------
def home(request):
    places = Place.objects.all()[:3]

    return render(
        request,
        "places/home.html",
        {
            "places": places,
        },
    )


# -------------------------
# Register
# -------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


# -------------------------
# Place List
# -------------------------
def place_list(request):
    query = request.GET.get("q")

    if query:
        places = Place.objects.filter(name__icontains=query)
    else:
        places = Place.objects.all()

    return render(
        request,
        "places/place_list.html",
        {
            "places": places,
        },
    )


# -------------------------
# Category Filter
# -------------------------
def category_places(request, category):
    places = Place.objects.filter(category=category)

    return render(
        request,
        "places/place_list.html",
        {
            "places": places,
            "category": category,
        },
    )


# -------------------------
# Place Detail + Reviews
# -------------------------
def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    if request.method == "POST":
        Review.objects.create(
            place=place,
            user_name=request.POST.get("user_name"),
            rating=request.POST.get("rating"),
            comment=request.POST.get("comment"),
        )

        return redirect("place_detail", place_id=place.id)

    return render(
        request,
        "places/place_detail.html",
        {
            "place": place,
        },
    )