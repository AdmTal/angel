from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from angel.settings import get_env_variable

from django.conf import settings

from .helpers import push_notification

from .models import Outfit, OutfitRating


def create(request, template):
    """Creates or returns form to create an outfit"""

    if request.method == 'POST':

        if 'message' in request.POST and 'picture' in request.FILES:
            outfit = Outfit(
                user=request.user,
                picture=request.FILES['picture'],
                message=request.POST['message']
            )

            outfit.save()

            ### Alert all friends that the outfit needs to be reviewed
            for friend in request.user.profile.friends.all():
                push_notification(friend.profile.pushover_key, title=request.POST['message'],
                                  message="{}/outfits/rate-an-outfit/{}".format(settings.DOMAIN, outfit.pk))

            return HttpResponseRedirect(reverse('view-outfit-rating', args=(outfit.pk,)))

        return render(request, template)
    else:
        return render(request, template)


@login_required
def view_rating(request, template, outfit_id):
    """Where a user can watch real time ratings of their outfits"""

    context = {
        'outfit': Outfit.objects.get(id=outfit_id),
        'pubnub_publish_key': get_env_variable('PUBNUB_PUBLISH_KEY'),
        'pubnub_subscribe_key': get_env_variable('PUBNUB_SUBSCRIBE_KEY'),
    }

    return render(request, template, context)


@login_required
def rate_an_outfit(request, template, outfit_id):
    """Where a user can rate their friends outfits"""
    if request.method == 'POST':
        ### CREATE OUTFIT RATING
        ### do some pubnub stuff...
        ### redirect to the thanks page
        rating = OutfitRating(user=request.user, score=request.POST['rating'], comment=request.POST['message'],
                              outfit=Outfit.objects.get(pk=outfit_id))

        rating.save()

        return render(request, 'thanks.html')
    else:
        context = {
            'outfit': Outfit.objects.get(id=outfit_id),
            'pubnub_publish_key': get_env_variable('PUBNUB_PUBLISH_KEY'),
            'pubnub_subscribe_key': get_env_variable('PUBNUB_SUBSCRIBE_KEY'),
        }
        return render(request, template, context)
