from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from projects.models import Permit, Project


def home(request):
    if not request.session['user_id']:
        return HttpResponseRedirect(reverse('users.views.login'))

    p = Permit.objects.filter(user_id=request.session['user_id'])

    return render_to_response('projects/home.html', {
        'user_id': request.session['user_id'],
        'projects': p
        })


def project(request, project_id):
    if not request.session['user_id']:
        return HttpResponseRedirect(reverse('users.views.login'))

    p = get_object_or_404(Project, pk=project_id)

    return render_to_response('projects/project.html', {
        'project': p
        })
