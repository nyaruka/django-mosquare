from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from mondays.models import MobileMonday, Event

def mondays(request, year=0, count=0):
    """
    Display mondays per given year, count or all
    """
    # Check if in this year Mobile monday were existing
    # and display that year's monday events
    # if year is 0 and count is more than 0 display last #count monday events
    # if this year is 0 and count is 0 display all monday events

    return render_to_response('mondays/mondays.html',
                              dict(),
                              context_instance=RequestContext(request))
