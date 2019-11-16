from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Simple App</h1><p>This is the simplest Django app that is possible.</p>")