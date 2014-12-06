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
    url(r'^WinterSchool/accommodation/', 'winSchool.views.accommodation'),
    url(r'^WinterSchool/transportation/', 'winSchool.views.transportation'),
    url(r'^WinterSchool/lectures/', 'winSchool.views.lectures'),
    url(r'^WinterSchool/download/', 'winSchool.views.download'),
    url(r'^WinterSchool/contact_us/', 'winSchool.views.contact_us'),
    url(r'^WinterSchool/registration/', 'winSchool.views.registration'),
    
    
)
