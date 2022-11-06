from rest_framework import serializers

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
        fields = ['low', 'high']


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
