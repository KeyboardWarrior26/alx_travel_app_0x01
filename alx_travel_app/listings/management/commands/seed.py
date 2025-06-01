from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
from decimal import Decimal
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed the database with Listings, Bookings, and Reviews"

    def handle(self, *args, **kwargs):
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        User.objects.all().exclude(is_superuser=True).delete()

        # Create users
        users = []
        for i in range(5):
            user = User.objects.create_user(
                username=f"user{i+1}",
                password="password123"
            )
            users.append(user)

        # Create Listings, Bookings, Reviews
        for i in range(5):
            listing = Listing.objects.create(
                name=f"Listing {i+1}",
                description="Sample description for listing",
                location="Cape Town",
                price_per_night=Decimal("100.00") + i
            )

            Booking.objects.create(
                listing=listing,
                user=users[i],
                start_date=date.today(),
                end_date=date.today() + timedelta(days=2),
            )

            Review.objects.create(
                listing=listing,
                user=users[i],
                rating=random.randint(1, 5),
                comment="Great experience!"
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded database."))

