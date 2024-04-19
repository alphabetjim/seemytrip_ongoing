from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Traveller(models.Model):
    """
    Stores an individual traveller, related to Django User model
    """
    user = models.OneToOneField(User, 
        on_delete = models.CASCADE,
        primary_key = True,)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    bio = models.TextField(max_length = 500)
    profile_photo = models.ImageField(upload_to = 'profileImages/',
        blank = True, default = 'placeholder')
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.user}: {self.firstname} {self.lastname} | created {self.created_on} | id: {self.pk}"