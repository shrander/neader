from django.conf.urls import patterns, include, url

from feeds import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<feed_id>\d+/$', views.detail, name='detail'),
)
