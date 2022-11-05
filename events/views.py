from rest_framework import generics

from events import serializers, models


class CompetitorsListView(generics.ListAPIView):
    """
    Returns a list of available competitors
    """
    queryset = models.CompetitorType.objects.all()
    serializer_class = serializers.CompetitorTypeSerializer


class OrganizerLevelListView(generics.ListAPIView):
    """
    Returns a list of available organizer's levels.
    """
    queryset = models.OrganizerLevel.objects.all()
    serializer_class = serializers.OrganizerLevelSerializer
