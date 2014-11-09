from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WinterSchool.winschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^WinterSchool/$', 'winSchool.views.home'),
    url(r'^WinterSchool/schedule/', 'winSchool.views.schedule'),
    url(r'^WinterSchool/hotel/', 'winSchool.views.hotel'),
    url(r'^WinterSchool/transport/', 'winSchool.views.transport'),
    url(r'^WinterSchool/professor/', 'winSchool.views.professor'),
    url(r'^WinterSchool/download/', 'winSchool.views.download'),
    url(r'^WinterSchool/about/', 'winSchool.views.about'),
    
    
    
)
