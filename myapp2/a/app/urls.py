from django.conf.urls import url
from notes.views import *



# URL patterns to match
urlpatterns = [
    url('notes', notes),
    url('test', test),
    url('page1', page1),
    url('', home),
]


