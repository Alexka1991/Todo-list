from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.todo, name='todo'),
    url(r'^form/$', views.todo_form, name='todo_form'),
    url(r'^del_todo/(?P<id>\d+)/$', views.del_todo, name='del_todo'),
]
