# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in"
                return HttpResponseRedirect('/feeds/')
            else:
                state = "Your account account is not active"
                # a better error message goes here
        else:
            state = "Your username and/or password were incorrect"
            # a better error message
    return render_to_response('auth/index.html',{'state':state, 'username':username}, context_instance=RequestContext(request))
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')