from rest_framework import generics

from events import serializers, models


class CompetitorsListView(generics.ListAPIView):
    queryset = models.CompetitorType.objects.all()
    serializer_class = serializers.CompetitorTypeSerializer
