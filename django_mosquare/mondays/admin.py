from django.contrib import admin
from mondays.models import Location, Participant, Sponsor, Organizer, Keynote, Event, Photo, MobileMonday

admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizer)
admin.site.register(Sponsor)
admin.site.register(Keynote)
admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(MobileMonday)
