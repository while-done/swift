from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'1', swift),
    url(r'^put_container/$', put_container),
    url(r'^delete_container/$', delete_container),
    url(r'^delete_object/$', delete_object),
    url(r'^put_object/$', put_object),
    url(r'^get_object/$', get_object),
    url(r'^put_objectfile/$', put_objectfile),
    url(r'^login/$', login),
    url(r'^loin/$', loin),

]