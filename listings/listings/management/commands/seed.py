from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        for i in range(10):
            Listing.objects.create(
                name=f"Listing {i}",
                description=f"Description for listing {i}",
                price_per_night=round(random.uniform(50, 300), 2),
                location=f"Location {i}"
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
