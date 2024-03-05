from rest_framework import generics, permissions
from coffee_social_api.permissions import IsOwnerOrReadOnly
from .models import Contact_admin
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    
    """
    Contacts List and Create a querie.
    """
    
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contact_admin.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    
    """
    Retrieve a querie, update or delete.
    """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactSerializer
    queryset = Contact_admin.objects.all()