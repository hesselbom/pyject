from django.db import models
from projects.models import Project
from users.models import User


class TodoManager(models.Manager):
    def create(self, description, time_estimate):
        return True


class Todo(models.Model):
    project = models.ForeignKey(Project)
    assigned_to = models.ForeignKey(User)
    description_short = models.CharField(max_length=140)
    description_long = models.CharField(max_length=1000)
    time_estimate = models.IntegerField()

    objects = TodoManager()
