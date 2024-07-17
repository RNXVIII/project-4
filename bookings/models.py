from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('booking_date', 'booking_time', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.booking_date} {self.booking_time}"
