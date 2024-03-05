from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from coffee_social_api.permissions import IsOwnerOrReadOnly
from .models import Barista
from .serializers import BaristaSerializer


class BaristaList(generics.ListCreateAPIView):

    """
    List of queries or create a comment if logged in.
    """

    serializer_class = BaristaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Calculate the total number of reviews and an average star-rating
    # related to each Barista.
    
    queryset = Barista.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'speciality_types',
        'location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaristaDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve a comment, or update or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BaristaSerializer
    queryset = Barista.objects.annotate(
        reviews_count = Count('reviews', distinct=True),
        average_rating = Avg('reviews__rating')
    ).order_by('-created_at')