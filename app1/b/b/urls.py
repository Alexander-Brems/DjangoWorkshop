from django.conf.urls import url
from app.views import home, test



# URL patterns to match
urlpatterns = [
    url('test', test),
    url('', home),
]


