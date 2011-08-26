from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from mondays.models import MobileMonday, Event

def home(request):
    """
    The main page
    """
    # Get the only mobile monday instance or create one
    try:
        mobilemonday = MobileMonday.objects.all()[0]
    except IndexError:
        # Redirect to the create mobile monday site
        # return HttpResponseRedirect(reverse('home'))
        pass

    # Get current or last event available
    current_or_last = Event.getCurrentOrLast()

    # if there is none
    if current_or_last is None:
        # Redirect to the create event pages
        # return HttpResponseRedirect(reverse('home'))        
        pass

    return render_to_response('home.html', 
                              dict(mobilmonday=mobilemonday,
                                   current_or_last=current_or_last),
                              context_instance=RequestContext(request))

def about(request):
    """
    The about Mobile monday page
    """
    pass
