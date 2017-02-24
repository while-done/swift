from django.conf.urls import include, url
from django.contrib import admin
from views import *
from nova import *
urlpatterns = [
    url(r'^role_delete/', role_delete),
    url(r'^role_update/', role_update),
    url(r'^role_create/', role_create),
    url(r'^group_delete/', group_delete),
    url(r'^group_update/', group_update),
    url(r'^group_create/', group_create),
    url(r'^user_delete/', user_delete),
    url(r'^user_update/', user_update),
    url(r'^user_create/', user_create),
    url(r'^project_delete/', project_delete),
    url(r'^project_update/', project_update),
    url(r'^project_create/', project_create),
    url(r'^glance_delete/', glance_delete),
    url(r'^glance_update/', glance_update),
    url(r'^glance_create/', glance_create),

    url(r'^nova/', nova),
    url(r'^nova_create/', nova_create),
    url(r'^nova_update/', nova_update),
    url(r'^nova_delete/', nova_delete),
    url(r'^nova_start/', nova_start),
    url(r'^nova_restart/', nova_restart),
    url(r'^nova_stop/', nova_stop),

]