from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.http import HttpResponse

def home(request):
    return HttpResponse('hey\n')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'counter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
)
