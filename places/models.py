from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):

    CATEGORY_CHOICES = [
        ('Forest', 'Forest'),
        ('Mountain', 'Mountain'),
        ('Temple', 'Temple'),
        ('Beach', 'Beach'),
        ('Waterfall', 'Waterfall'),
        ('Historical', 'Historical'),
        ('Food', 'Food Destination'),
    ]

    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Forest'
    )

    image = models.ImageField(
        upload_to='places/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class FoodSpot(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    special_food = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Stay(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    price_per_night = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE
    )

    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.user_name


# -----------------------------
# NEW: Place Suggestion
# -----------------------------
class PlaceSuggestion(models.Model):

    CATEGORY_CHOICES = [
        ('Forest', 'Forest'),
        ('Mountain', 'Mountain'),
        ('Temple', 'Temple'),
        ('Beach', 'Beach'),
        ('Waterfall', 'Waterfall'),
        ('Historical', 'Historical'),
        ('Food', 'Food Destination'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    taluk = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="suggestions/",
        blank=True,
        null=True
    )

    # NEW: Admin approval status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.user.username}"