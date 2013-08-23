from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from edit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<paper_id>\d+)/$', views.edit, name='edit'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^submitfeedback/$', views.submitfeedback, name='feedback'),
    url(r'^createuser/$', views.createuser, name='createuser'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^submitpaper/$', views.submitpaper, name='submitpaper'),
)