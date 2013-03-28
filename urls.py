   #Copyright 2013 Aaron Curtis

   #Licensed under the Apache License, Version 2.0 (the "License");
   #you may not use this file except in compliance with the License.
   #You may obtain a copy of the License at

       #http://www.apache.org/licenses/LICENSE-2.0

   #Unless required by applicable law or agreed to in writing, software
   #distributed under the License is distributed on an "AS IS" BASIS,
   #WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   #See the License for the specific language governing permissions and
   #limitations under the License.

from django.conf.urls import patterns, include, url
from django.views.generic.list_detail import *
from django.contrib import admin
from logbrowse.models import Flight
from logbrowse.views import *
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'afterflight2.views.home', name='home'),
    # url(r'^afterflight2/', include('afterflight2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #url(r'^flight/(?P<slug>.+)/$',object_detail,{'queryset':Flight.objects.all()}, name='flights'),
    url(r'^flight/(?P<slug>.+)/$',flightDetail, name='flights'),
    url(r'^tg_timeline/$',timegliderFormatFlights, name='timeline'),
    url(r'^flight/$',flightIndex, name='timeline'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes':True
        }),
    )