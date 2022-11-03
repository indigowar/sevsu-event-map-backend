from django.db import models


class OrganizerLevel(models.Model):
    """
    OrganizerLevel model contains information about a level of organizer.

    For example, Federal, Regional and Educational levels of organizers.
    """
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=3)


class Organizer(models.Model):
    """
    Organizer model contains info about one organizer of event.
    """
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=512)
    level = models.ForeignKey(OrganizerLevel, on_delete=models.CASCADE)


class FoundingRange(models.Model):
    """
    FoundingRange contains two integer, the low(minimal) value of a range and the high(maximum) value.
    """
    low = models.IntegerField()
    high = models.IntegerField()


class FoundingType(models.Model):
    """
    FoundingType contains information about type of founding.

    For example, a grant or a loan.
    """
    name = models.CharField(max_length=255, blank=False)


class CoFoundingRange(models.Model):
    """
    CoFoundingRange contains a minimal and maximum percent of money that should be invested
    by other investors then Organizer of Event.
    """
    low = models.IntegerField()
    high = models.IntegerField()


class Event(models.Model):
    """
    Event model is the main model of the app.

    It contains information about actual event.
    """
    title = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    founding_type = models.ManyToManyField(FoundingType)
    founding_range = models.OneToOneField(FoundingRange, on_delete=models.CASCADE)
    co_founding_range = models.OneToOneField(CoFoundingRange, on_delete=models.CASCADE)
    submission_deadline = models.DateTimeField()
    consideration_period = models.DateField()
    realisation_period = models.DateField()
    result = models.TextField()
    site = models.CharField(max_length=512)
    document = models.CharField(max_length=512)
    internal_university_contacts = models.CharField(max_length=512)
    tlr_value = models.IntegerField()


class CompetitorType(models.Model):
    """
    CompetitorType model contains a name for competitor type.

    For example, One Person, a Group or a company.
    """
    name = models.CharField(max_length=255)


class EventRequirementMapping(models.Model):
    """
    EventRequirement it's a mapping that defines a link
    between an event and a competitor type this event require.
    """
    competitor = models.ManyToManyField(CompetitorType)
    event = models.ManyToManyField(Event)


class EventSubject(models.Model):
    """
    EventSubject model defines a subject that some event has.
    """
    subject = models.CharField(max_length=255, blank=False)
    event = models.ManyToManyField(Event)


class EventPrecursor(models.Model):
    """
    If the event has a precursor(the event you should pass before get into this event), then this model
    defines a link between them.
    """
    event_precursor = models.ManyToManyField(Event, related_name='event_precursor')
    successor = models.ManyToManyField(Event, related_name='current_event')
