from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

location = models.CharField(max_length=255, default='Unknown Location')
