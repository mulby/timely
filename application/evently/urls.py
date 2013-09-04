from django.conf.urls import patterns, url
from evently.views import EventList

urlpatterns = patterns(
    '',
    url(r'^$', EventList.as_view()),
)
