from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class FoodSpot(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
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