from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('edit.urls')),

    # url(r'^$', 'peer_edit.views.home', name='home'),
    # url(r'^peer_edit/', include('peer_edit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# from django.conf import settings

# urlpatterns += patterns('',
#     url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views', {
#         'document_root': settings.STATIC_ROOT,
#     }),
#  )
