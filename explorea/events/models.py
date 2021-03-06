from django.db import models
from django.conf import settings
from datetime import datetime as dt


class Event(models.Model):
    FUN = 'FN'
    RELAX = 'RX'
    EXP = 'EX'
    SIGHTS = 'SI'

    CATEGORY_CHOICES= (
        (FUN, 'fun'),
        (RELAX, 'relax'),
        (EXP, 'experience'),
        (SIGHTS, 'sights')
    )

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=500)
    category = models.CharField(
        max_length=20,
        choices = CATEGORY_CHOICES,
        default = FUN,
    )
    host = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        

class EventRun(models.Model):

    event = models.ForeignKey(Event, 
        on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False) #TODO there shouldnt be default???
    time = models.TimeField(blank=False, null=False)
    seats_available = models.PositiveIntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, 
        decimal_places=2, blank=False, null=False)