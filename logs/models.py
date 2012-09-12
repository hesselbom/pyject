from django.db import models
from users.models import User


class LogManager(models.Manager):
    def add(self, event, user):
        log_entry = self.create(event=event, user_id=user)

        return log_entry


class Log(models.Model):
    event = models.CharField(max_length=140)
    event_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User)

    objects = LogManager()

    def __unicode__(self):
        return self.event
