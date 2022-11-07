from rest_framework import generics

from events.models import OrganizerLevel, Organizer
from events.serializers import OrganizerSerializer, OrganizerLevelSerializer


class LevelsListAPIView(generics.ListAPIView):
    """
    returns a list of available organizer's levels.
    """
    queryset = OrganizerLevel.objects.all()
    serializer_class = OrganizerLevelSerializer


class __OrganizerView(generics.GenericAPIView):
    """
    A base class for views that uses Organizer as a model
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class ListCreateAPIView(__OrganizerView, generics.ListCreateAPIView):
    """
    On GET returns a list of available organizers.
    On POST adds new organizer.
    """


class RetrieveUpdateDestroyAPIView(__OrganizerView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET returns information about organizer.
    On PUT updates an organizer info.
    On DELETE deletes this organizer.
    """
