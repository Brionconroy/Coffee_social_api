from django.db import models
from django.contrib.auth.models import User
from barista.models import Barista


class Review(models.Model):

    ONE_TO_FIVE_RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
     )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    barista = models.ForeignKey(
        Barista, on_delete=models.CASCADE, related_name='reviews'
    )
    content = models.TextField()
    rating = models.IntegerField(choices=ONE_TO_FIVE_RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}' review"
