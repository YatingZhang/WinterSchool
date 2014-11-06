from django.conf.urls import patterns, include, url

from django.contrib import admin
from winSchool.views import register
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WinterSchool.winschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^WinterSchool/register/', 'winSchool.views.register'),
    url(r'^WinterSchool/', 'winSchool.views.home'),
    
)
