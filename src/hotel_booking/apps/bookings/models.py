from django.db import models

class Booking(models.Model):
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        db_table = 'bookings'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(date_start__lt=models.F('date_end')),
                name='check_date_range'
            )
        ]

    def __str__(self):
        return f"Booking {self.id} for Room {self.room.id}"