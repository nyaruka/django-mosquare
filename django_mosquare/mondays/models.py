from datetime import date
from django.db import models
from settings import MEDIA_ROOT

class Location(models.Model):
    """
    Event location details
    """
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=20, decimal_places=16)
    longitude = models.DecimalField(max_digits=20, decimal_places=16)

    def __unicode__(self):
        return self.name

class Participant(models.Model):
    """
    Broad definition of individues part of mobile monday
    """
    GENDER_CHOICES = (('M', "MALE"),
                      ('F', "FEMALE"))
    lastname = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    title = models.CharField(max_length=64)
    email = models.EmailField()
    institution = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        return "Participant_%s" % self.lastname

class Organizer(Participant):
    """
    In addition to participant details
    """
    google = models.CharField(max_length=64, null=True, blank=True)
    twitter = models.CharField(max_length=64, null=True, blank=True)
    linkedin = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()

class Sponsor(models.Model):
    """
    Any company with short or long term commitment to mobile monday in terms
    of money sponsorship or any other action making momo go forward
    """
    COMMITMENT_CHOICES = (('SPONSOR', "SPONSOR"),
                          ('PARTNER', "PARTNER"))
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=MEDIA_ROOT)
    commitment = models.CharField(max_length=64, default='SPONSOR', choices=COMMITMENT_CHOICES)

    def __unicode__(self):
        return "%s_%s" % (self.commitment, self.name)

class Keynote(models.Model):
    """
    Keynote elements
    """
    topic = models.CharField(max_length=200)
    description = models.TextField()
    presenter = models.OneToOneField(Participant)
    start = models.TimeField()
    end = models.TimeField()
    order = models.IntegerField()

    def __unicode__(self):
        return "%s_keynote" % self.presenter.lastname

class Event(models.Model):
    """
    Details on monday events
    """
    date = models.DateField(max_length=64)
    location = models.OneToOneField(Location)
    sponsors = models.ManyToManyField(Sponsor)
    presentations = models.ManyToManyField(Keynote)

    def __unicode__(self):
        return "%s" % self.location.name

    @classmethod
    def getClosed(cls):
        return Event.objects.filter(date__lt=date.today())

    @classmethod
    def getOpen(cls):
        return Event.objects.filter(date__gt=date.today())

    @classmethod
    def getCurrentOrLast(cls):
        open = Event.getOpen()
        closed = Event.getClosed()
        if open:
            return open[0]
        elif closed:
            last = len(closed) - 1
            return closed[last]

class Photo(models.Model):
    """
    All Photos relating to passed events
    """
    photo = models.ImageField(upload_to=MEDIA_ROOT +"/photos")
    caption = models.CharField(max_length=200, null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)

    def __unicode__(self):
        return self.caption

class MobileMonday(models.Model):
    """
    General recembrance of these events
    """
    year_started = models.DateField(max_length=4)
    residence_city = models.CharField(max_length=64)
    cityscape_logo = models.ImageField(upload_to=MEDIA_ROOT)
    organizers = models.ManyToManyField(Organizer)

    def __unicode__(self):
        return "momo_%s" % self.residence_city

    def birthmonday(self):
        """
        The nearest next monday of the current birthday
        """
        pass
