from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WinterSchool.winschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^WinterSchool/$', 'winSchool.views.home'),
    url(r'^WinterSchool/page1/', 'winSchool.views.page'),
    url(r'^WinterSchool/page2/', 'winSchool.views.page2'),
    
)
