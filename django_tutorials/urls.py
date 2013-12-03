from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorials.views.home', name='home'),
    #url(r'^blog/', views.list_schools),
    url(r'^schools/', 'colleges.views.list_schools'),

    url(r'^admin/', include(admin.site.urls)),
)