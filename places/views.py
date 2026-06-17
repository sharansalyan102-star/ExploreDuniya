from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import (
    Place,
    Review,
    PlaceSuggestion,
)


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
from django.db.models import Q

def place_list(request):
    query = request.GET.get("q", "")

    places = Place.objects.all()

    if query:
        places = places.filter(
            Q(name__icontains=query) |
            Q(state__icontains=query) |
            Q(district__icontains=query) |
            Q(taluk__icontains=query)
        )

    return render(
        request,
        "places/place_list.html",
        {
            "places": places,
            "query": query,
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
@login_required
def suggest_place(request):
    if request.method == "POST":
        PlaceSuggestion.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            state=request.POST.get("state"),
            district=request.POST.get("district"),
            taluk=request.POST.get("taluk"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
        )

        return render(
            request,
            "places/suggest_success.html",
        )

    return render(
        request,
        "places/suggest_place.html",
    )