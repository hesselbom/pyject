from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=92)
    client = models.CharField(max_length=92)

    def __unicode__(self):
        return self.name


class Permit(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)


class Todo(models.Model):
    project_id = models.ForeignKey(Project)
    assigned_to = models.ForeignKey(User)
    description_short = models.CharField(max_length=140)
    description_long = models.CharField(max_length=1000)
    time_estimate = models.IntegerField()
