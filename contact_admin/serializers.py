from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact_admin


class ContactSerializer(serializers.ModelSerializer):

    """
    Serializer for the Contact model
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):

        """
        Returns a time stamp with better readablity
        """

        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):

        """
        Returns a time stamp for updates
        with better readablity
        """

        return naturaltime(obj.updated_at)

    class Meta:

        """
        List of fields to be retrived by Api
        """

        model = Contact_admin
        fields = [
            "id",
            "profile_id",
            "profile_image",
            "owner",
            "queries",
            "content",
            "created_at",
            "updated_at",
        ]
