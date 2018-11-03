from django.db import models

# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=500)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name