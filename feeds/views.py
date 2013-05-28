# Create your views here.


from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    state = ''
    if request.user.is_authenticated():
        #do stuff
        state = request.user.username +": Logged In"
    else:
        state = 'Not logged in!'
        HttpResponseRedirect('/')

    return render_to_response('feeds/index.html',
    {'state':state, 'username':request.user.get_username()}, 
    context_instance=RequestContext(request))