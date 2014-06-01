from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^create/$', 'outfits.views.create', {'template': 'create_outfit.html'}, name='create_outfit'),
                       url(r'^view-outfit-rating/(?P<outfit_id>\d+)/', 'outfits.views.view_rating', {'template': 'view_outfit_rating.html'}, name='view-outfit-rating'),
                       url(r'^rate-an-outfit/(?P<outfit_id>\d+)/', 'outfits.views.rate_an_outfit', {'template': 'rate_an_outfit.html'}, name='rate-an-outfit'),
)
