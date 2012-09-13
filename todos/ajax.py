from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from todos.models import Todo
from logs.models import Log
from users.models import User

@dajaxice_register
def save_todo(request):
    user = User.objects.get(pk=request.session['user_id'])

    l = Log.objects
    l.add(user.username, user)
