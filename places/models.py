from django.db import models

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
        return self.user_name    


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
