from rest_framework import generics

from events.models import CompetitorType
from events.serializers import CompetitorTypeSerializer


class ListView(generics.ListAPIView):
    """
    Returns a list of available competitors
    """
    queryset = CompetitorType.objects.all()
    serializer_class = CompetitorTypeSerializer
