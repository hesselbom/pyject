from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from users.models import Auth


def login(request):
    return render_to_response('users/login.html',
        context_instance=RequestContext(request))


def logout(request):
    request.session['user_id'] = False

    return HttpResponseRedirect(reverse('users.views.login'))


def validate(request):
    username = request.POST['email']
    password = request.POST['password']

    a = Auth()
    valid = a.initiate(username, password)

    if valid:
        request.session['user_id'] = valid
        return HttpResponseRedirect(reverse('projects.views.home'))
    else:
        return render_to_response('users/login.html', {
            'error_message': 'Wrong username or password.'
            }, context_instance=RequestContext(request))


def dash(request):
    return render_to_response('users/dash.html', {
        'user_id': request.session['user_id']
        })
