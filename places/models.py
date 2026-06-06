from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name