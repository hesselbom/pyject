from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=75)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __unicode__(self):
        return self.username
