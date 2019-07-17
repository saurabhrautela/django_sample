# used to create APIs that work closely with models
# as much of the functionality is already implemented
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# used to add filtering to the viewset
from rest_framework import filters

from profiles import serializers
from profiles import models
from profiles import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and handling APIs."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    # searching will be done on the basis of these fields
    search_fields = ("name", "fields",)
