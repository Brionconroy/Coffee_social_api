from rest_framework import serializers
from .models import Barista


class BaristaSerializer(serializers.ModelSerializer):

    """
    Barista serializer to add the owners profile image
    and fields to hold the number of reviews related to that
    User and calculation of average star-rating.
    """
    
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    review_count = serializers.ReadOnlyField()
    star_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):

        """
        Returns true if the user making the request
        is the owner of the Barista
        """

        request = self.context['request']
        return request.user == obj.owner

    class Meta:

        """
        Lists all the data fields to be
        returned by this API
        """

        model = Barista
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'location', 'speciality_types', 'rates_per_hour', 
            'email', 'created_at', 'updated_at',
            'review_count', 'star_rating',
        ]