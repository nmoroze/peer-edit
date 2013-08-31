from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from edit import views, utils

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<paper_id>\d+)/$', views.edit, name='edit'),
    url(r'^bestfeedback/(?P<feedback_id>\d+)/$', views.feedback, name='bestfeedback'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^submitfeedback/$', views.submitfeedback, name='feedback'),
    url(r'^createuser/$', views.createuser, name='createuser'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^submitpaper/$', views.submitpaper, name='submitpaper'),
    url(r'^accounts/profile/$', views.index, name='indexfromfailedlogin'),

    url(r'^paper/save/$', utils.papersave, name='token'),
    url(r'^feedback/save/$', utils.feedbacksave, name='token'),
    url(r'^feedback/delete/$', utils.delete, name='token'),
)
