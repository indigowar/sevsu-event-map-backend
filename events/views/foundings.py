from rest_framework import generics

from events.models import FoundingType, FoundingRange, CoFoundingRange
from events.serializers import FoundingTypeSerializer, FoundingRangeSerializer, CoFoundingRangeSerializer


class __RangeView(generics.GenericAPIView):
    """
    A base class for views that uses Founding Range as a model
    """
    queryset = FoundingRange.objects.all()
    serializer_class = FoundingRangeSerializer


class TypeListView(generics.ListAPIView):
    """
    Returns a list of available founding types.
    """
    queryset = FoundingType.objects.all()
    serializer_class = FoundingTypeSerializer


class FoundingRangeListCreateAPIView(__RangeView, generics.ListCreateAPIView):
    """
    On GET - returns a list of founding ranges.
    On POST - adds new founding range
    """


class FoundingRangeRetrieveUpdateDestroyView(__RangeView, generics.RetrieveUpdateDestroyAPIView):
    """
    On GET return a range
    On POST updates a range
    On DELETE deletes a range
    """


class CoFoundingRangeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    On GET return a range
    On POST updates a range
    On DELETE deletes a range
    """
    queryset = CoFoundingRange
    serializer_class = CoFoundingRangeSerializer


class CoFoundingCreateAPIView(generics.CreateAPIView):
    """
    On POST adds a new co-founding range
    """
    queryset = CoFoundingRange
    serializer_class = CoFoundingRangeSerializer
