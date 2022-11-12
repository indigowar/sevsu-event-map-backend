from rest_framework import serializers
from django.db import transaction

from events import models


class OrganizerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizerLevel
        fields = ['id', 'name', 'code']
        read_only_fields = ['id']


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizer
        fields = ['id', 'name', 'logo', 'level']
        read_only_fields = ['id']


class NestedOrganizerSerializer(OrganizerSerializer):
    level = OrganizerLevelSerializer()


class RangeSerializer(serializers.ModelSerializer):
    """
    A Serializer for classes that have only low and high fields integer fields.
    """

    class Meta:
        fields = ['id', 'low', 'high']
        read_only_fields = ['id']


class FoundingRangeSerializer(RangeSerializer):
    class Meta(RangeSerializer.Meta):
        model = models.FoundingRange


class CoFoundingRangeSerializer(RangeSerializer):
    class Meta(RangeSerializer.Meta):
        model = models.CoFoundingRange


class FoundingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoundingType
        fields = ['id', 'name']
        read_only_fields = ['id']


class CompetitorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompetitorType
        fields = ['id', 'name']
        read_only_fields = ['id']


class MinimalEventSerializer(serializers.ModelSerializer):
    """
    This serializer serialize only data that required to draw
    Event on the map.
    """

    class Meta:
        model = models.Event
        fields = ['id', 'organizer', 'title', 'submission_deadline', 'tlr']
        read_only_fields = ['id']


class MinimalNestedEventSerializer(MinimalEventSerializer):
    """
    This serializer serialize only data that required to draw
    Event on the map.

    But does this nested. So the organizer is not a key, it's a structure
    """
    organizer = NestedOrganizerSerializer()


class EventSerializer(serializers.ModelSerializer):
    """
    Serialize event.
    """

    class Meta:
        model = models.Event
        fields = [
            'id',
            'organizer',
            'founding_type',
            'founding_range',
            'co_founding_range',
            'submission_deadline',
            'consideration_period',
            'realisation_period',
            'result',
            'site',
            'document',
            'internal_university_contacts',
            'tlr'
        ]
        read_only_fields = ['id']


class NestedEventSerializer(EventSerializer):
    """
    Serialize event, but with nested structures.
    """
    organizer = NestedOrganizerSerializer()
    founding_type = FoundingTypeSerializer()
    founding_range = FoundingRangeSerializer()
    co_founding_range = CoFoundingRangeSerializer()


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventSubject
        fields = ['id', 'subject', 'event']
        read_only_fields = ['id']


class FullEventInfoSerializer(serializers.ModelSerializer):
    # the id of event
    id = serializers.IntegerField()

    organizer = NestedOrganizerSerializer()
    founding_type = serializers.IntegerField()
    founding_range = FoundingRangeSerializer()
    co_founding_range = CoFoundingRangeSerializer()

    # submission deadline is a real date and time
    submission_deadline = serializers.DateTimeField()

    # Consideration
    #
    # The result consideration_period in event will be:
    # CP = 1970 + Consideration_period * consideration_measure
    consideration_measure = serializers.IntegerField()
    consideration_period = serializers.IntegerField()

    # same as Consideration
    realisation_measure = serializers.IntegerField()
    realisation_period = serializers.IntegerField()

    result = serializers.CharField(max_length=2048*2048)
    site = serializers.CharField(max_length=1024)
    document = serializers.CharField(max_length=1024)
    internal_university_contacts = serializers.CharField(max_length=1024)

    tlr = serializers.IntegerField()

    @transaction.atomic
    def create(self, validated_data):
        organizer = models.Organizer.objects.filter(name=validated_data['name'])
        return super(FullEventInfoSerializer, self).create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        return super(FullEventInfoSerializer, self).update(validated_data)
