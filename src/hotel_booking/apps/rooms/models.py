from django.db import models

class Room(models.Model):
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rooms'

    def __str__(self):
        return f"Room {self.id}: {self.description}"