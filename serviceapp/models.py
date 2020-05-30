from django.db import models
from django.contrib.auth.models import User

class TruckSchedule(models.Model):
    truckId = models.CharField(max_length=128, blank = True, null = True)
    orderId = models.CharField(max_length=256, blank = True, null = True)
    sourceCity = models.CharField(max_length=128, blank = True, null = True)
    destinationCity = models.CharField(max_length=128, blank=True, null=True)
    departureDate = models.CharField(max_length=128, blank=True, null=True)
    arrivalDate = models.CharField(max_length=128, blank=True, null=True)
    scheduledAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.truckId
