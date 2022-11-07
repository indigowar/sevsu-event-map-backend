from rest_framework import generics

from events.models import Event
from events.serializers import EventSerializer, MinimalEventSerializer


class __EventView(generics.GenericAPIView):
    """
    A Base class for Views that uses Event as a model
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MinimalRetrieveAPIView(__EventView, generics.RetrieveAPIView):
    """
    Returns a minimal info that required to be drawn.
    """
    serializer_class = MinimalEventSerializer


class RetrieveUpdateDestroyAPIView(__EventView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET returns a full view
    On POST updates a view
    ON DELETE deletes a view
    """


class ListCreateAPIView(__EventView, generics.ListCreateAPIView):
    """
    On GET - returns all events.
    On POST - adds a new one.
    """
