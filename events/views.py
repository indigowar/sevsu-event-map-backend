from rest_framework import generics

from events import serializers, models


class OrganizerView(generics.GenericAPIView):
    """
    A base class for views that uses Organizer as a model
    """
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class FoundingRangeView(generics.GenericAPIView):
    """
    A base class for views that uses Founding Range as a model
    """
    queryset = models.FoundingRange.objects.all()
    serializer_class = serializers.FoundingRangeSerializer


class EventView(generics.GenericAPIView):
    """
    A Base class for Views that uses Event as a model
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


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


class OrganizerListCreateView(OrganizerView, generics.ListCreateAPIView):
    """
    On GET returns a list of available organizers.
    On POST adds new organizer.
    """


class OrganizerRetrieveUpdateDestroyView(OrganizerView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET returns information about organizer.
    On PUT updates an organizer info.
    On DELETE deletes this organizer.
    """


class FoundingRangeListCreateAPIView(FoundingRangeView, generics.ListCreateAPIView):
    """
    Returns a list of founding ranges.
    """


class FoundingRangeRetrieveUpdateDestroyView(FoundingRangeView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET return a range
    On POST updates a range
    On DELETE deletes a range
    """


class MinimalEventView(EventView, generics.RetrieveAPIView):
    """
    Returns a minimal info that required to be drawn.
    """
    serializer_class = serializers.MinimalEventSerializer


class EventView(EventView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET returns a full view
    On POST updates a view
    ON DELETE deletes a view
    """
