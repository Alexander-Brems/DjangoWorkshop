from django.conf.urls import url
from notes.views import Notes

urlpatterns = [
    url('', Notes.as_view()),
]
