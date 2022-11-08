from rest_framework import generics

from events.models import EventSubject
from events.serializers import SubjectSerializer


class __SubjectView(generics.GenericAPIView):
    queryset = EventSubject.objects.all()
    serializer_class = SubjectSerializer


class ListCreateAPIView(__SubjectView, generics.ListCreateAPIView):
    pass


class ListByEventAPIView(__SubjectView, generics.ListAPIView):
    def get_queryset(self):
        return super().get_queryset().filter(event=self.event)

    @property
    def event(self):
        return self.kwargs['event']


class RetrieveUpdateDestroyAPIView(__SubjectView, generics.RetrieveUpdateDestroyAPIView):
    """

    """
