from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from users.models import User


def login(request):
    return render_to_response('users/login.html',
        context_instance=RequestContext(request))


def validate(request):
    get_object_or_404(User)

    username = request.POST['email']
    password = request.POST['password']

    with_username = User.objects.filter(username__exact=username, password__exact=password)
    with_email = User.objects.filter(email__exact=username, password__exact=password)

    if with_username:
        success = with_username
    elif with_email:
        success = with_email
    else:
        return render_to_response('users/login.html', {
            'error_message': 'Wrong username or password.'
            }, context_instance=RequestContext(request))

    if success:
        request.session['user_id'] = success
        return HttpResponseRedirect(reverse('users.views.dash'))


def dash(request):
    return render_to_response('users/dash.html', {
        'user_id': request.session['user_id']
        })
