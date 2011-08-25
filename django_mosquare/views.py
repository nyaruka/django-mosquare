from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from mondays.model import *

def home(request):
    """
    The main page
    """
    # Get the only mobile monday instance

    # Get the next event if not available get current and
    # send email to the admin reminding him to create the next event
    # If there are possibility that many event are already there in advance
    # make sure that you get the next from now

    return render_to_response('home.html', 
                              dict(),
                              context_instance=RequestContext(request))

    
def about(request):
    """
    The about Mobile monday page
    """
    pass
