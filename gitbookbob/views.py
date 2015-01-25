import json, subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    event_json = json.loads(request.body)

    if event_json['repository']['name'] == 'tutorial':
        subprocess.call(['/home/django/tutorial/update.sh'])

    if event_json['repository']['name'] == 'tutorial-extensions':
        subprocess.call(['/home/django/tutorial-extensions/update.sh'])

    if event_json['repository']['name'] == 'coach-manual':
        subprocess.call(['/home/django/coach-manual/update.sh'])

    if event_json['repository']['name'] == 'organizer-manual':
        subprocess.call(['/home/django/organizer-manual/update.sh'])

    return HttpResponse(status=200)
