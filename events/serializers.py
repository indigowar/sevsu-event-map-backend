from rest_framework import serializers

from events import models


class OrganizerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizerLevel
        fields = ['name', 'code']


class OrganizerSerializer(serializers.ModelSerializer):
    level = OrganizerLevelSerializer()

    class Meta:
        model = models.Organizer
        fields = ['name', 'logo', 'level']


class RangeSerializer(serializers.ModelSerializer):
    """
    A Serializer for classes that have only low and high fields integer fields.
    """

    class Meta:
        fields = ['low', 'high']


class FoundingRangeSerializer(RangeSerializer):
    class Meta:
        model = models.FoundingRange


class CoFoundingRangeSerializer(RangeSerializer):
    class Meta:
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

    organizer = OrganizerSerializer()

    class Meta:
        model = models.Event
        fields = ['id', 'organizer', 'title', 'submission_date', 'tlr']


# class FullEventSerializer(serializers.ModelSerializer):
#     organizer = OrganizerSerializer()
#     founding_type = FoundingTypeSerializer()
#     founding_range = FoundingRangeSerializer()
#     co_founding_range = CoFoundingRangeSerializer()
#
#     class Meta:
#         model = models.Event
#         fields = [
#             'id', 'title', 'organizer', 'founding_type',
#             'founding_range', 'co_founding_range',
#             'submission_deadline', 'consideration_period',
#             'realisation_period', 'result', 'site', 'document',
#             'internal_university_contacts', 'tlr',
#
#             'requirements', 'subjects'
#         ]
#         read_only_fields = ['id']
