from django.shortcuts import render_to_response, get_object_or_404
from projects.models import Permit, Project


def home(request):
    # p = get_object_or_404(Permit, user_id=request.session['user_id'])
    p = Permit.objects.filter(user_id=request.session['user_id'])
    # projects = p.objects.all()
    return render_to_response('projects/home.html', {
        'user_id': request.session['user_id'],
        'projects': p
        })


def project(request, project_id):
    p = get_object_or_404(Project, pk=project_id)

    return render_to_response('projects/project.html', {
        'project': p
        })
