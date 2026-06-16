from django.contrib import admin
from .models import (
    Place,
    FoodSpot,
    Stay,
    Review,
    PlaceSuggestion,
)


@admin.action(description="Approve selected suggestions")
def approve_suggestions(modeladmin, request, queryset):
    for suggestion in queryset:

        # Create a new Place
        Place.objects.create(
            name=suggestion.name,
            state=suggestion.state,
            description=suggestion.description,
            category=suggestion.category,
            image=suggestion.image,
        )

        # Mark suggestion as approved
        suggestion.status = "Approved"
        suggestion.save()


@admin.register(PlaceSuggestion)
class PlaceSuggestionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "state",
        "district",
        "taluk",
        "category",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "state",
    )

    search_fields = (
        "name",
        "state",
        "district",
        "taluk",
    )

    actions = [approve_suggestions]


# Register remaining models
admin.site.register(Place)
admin.site.register(FoodSpot)
admin.site.register(Stay)
admin.site.register(Review)