from django.db import models
from django.contrib.auth.models import User
from travellerprofile.models import Traveller
from trips.models import Trip

# Create your models here.
class TripComment(models.Model):
    """
    Stores a single user comment on a trip
    """
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "tripcomments")
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name = "tripcomments")
    body = models.TextField(max_length = 500)
    likes = models.ManyToManyField(User, related_name = 'liked', blank = True)
    approved = models.BooleanField(default = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.pk}: {self.author} comment on {self.trip} at {self.created_on}"