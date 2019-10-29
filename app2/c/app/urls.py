from django.conf.urls import url
from notes.views import home, missing, notes, test, unc



# URL patterns to match
urlpatterns = [
    url('home', home),
    url('notes', notes),
    url('test', test),
    url('unc',  unc),
    url('', missing),
]


