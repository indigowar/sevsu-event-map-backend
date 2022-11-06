from rest_framework import generics, mixins

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


class FoundingTypeListView(generics.ListAPIView):
    """
    Returns a list of available founding types.
    """
    queryset = models.FoundingType.objects.all()
    serializer_class = serializers.FoundingTypeSerializer


class OrganizerListCreateView(generics.ListCreateAPIView):
    """
    On GET returns a list of available organizers.
    On POST adds new organizer.
    """
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class MinimalEventView(generics.RetrieveAPIView):
    """
    Returns a minimal info that required to be drawn.
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.MinimalNestedEventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EventView(generics.RetrieveUpdateDestroyAPIView):
    """
    On GET returns a full view
    On POST updates a view
    ON DELETE deletes a view
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
