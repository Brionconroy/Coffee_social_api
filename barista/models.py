from django.db import models
from django.contrib.auth.models import User


class Barista(models.Model):

    """
    Barista model
    """
    
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality_types = models.CharField(max_length=255)
    rates_per_hour = models.IntegerField()
    location = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        """
        Ordered the objects by first created 
        """

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s Barista Details"