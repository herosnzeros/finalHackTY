from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.contrib import admin
from dsite.views import index, profile
admin.autodiscover()

from dsite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heroes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^homepage', index),
    url(r'^profile/$', profile),
    url(r'^login/$', login , {"template_name":"login.html"}),
)
