from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'angel.views.home', {'template': 'home.html'}, name='home'),
                       url(r'^about/$', 'angel.views.about', {'template': 'about.html'}, name='about'),
                       url(r'^register/$', 'users.views.register', {'template': 'register.html'}, name='register'),
                       url(r'^login/$', 'users.views.user_login', {'template': 'login.html'}, name='login'),
                       url(r'^logout/$', 'users.views.user_logout', name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^outfits/', include('outfits.urls'))
)


if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(.*)$', 'django.views.static.serve',
                                kwargs={'document_root': settings.MEDIA_DIR}),
                            url(r'^500/$', 'django.views.defaults.server_error'),
                            url(r'^404/$', 'django.views.defaults.page_not_found'),
    )