from django.db import models
import hashlib


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=75)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __unicode__(self):
        return self.username


class Auth():
    def initiate(self, username, password):
        h = hashlib.sha512()
        h.update('45etrgfd')
        h.update(password)
        h.update('ag8e4s@')

        password_hash = h.hexdigest()
        print password_hash

        username_auth = User.objects.filter(username__exact=username, password__exact=password_hash)
        email_auth = User.objects.filter(email__exact=username, password__exact=password_hash)

        if username_auth:
            user_id = username_auth[0].id
            return user_id
        elif email_auth:
            user_id = email_auth[0].id
            return user_id
        else:
            return False
