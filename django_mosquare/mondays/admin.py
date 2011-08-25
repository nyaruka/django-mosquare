from django.contrib import admin
from mondays.models import Location, Sponsor, Participant, Keynote, Event, MobileMonday

admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Sponsor)
admin.site.register(Keynote)
admin.site.register(Event)
admin.site.register(MobileMonday)
