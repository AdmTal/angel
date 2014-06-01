from django.db import models
from django.contrib.auth.models import User
###
from angel.models import BaseModel


class Outfit(BaseModel):
    """A picture of a users outfit, to be rated by a group of trusted friends"""
    user = models.ForeignKey(User, related_name='outfits')
    picture = models.ImageField(upload_to='outfit_images', blank=True, help_text='picture of outfit')
    message = models.CharField(max_length='256', blank=True, help_text='message to include with picture')

    def __unicode__(self):
        return "{} -- {}".format(self.user, self.message)


class OutfitRating(BaseModel):
    """A users rating for an outfit"""
    user = models.ForeignKey(User, related_name='ratings')
    score = models.IntegerField()
    comment = models.CharField(max_length='256', blank=True, help_text='Comment to include with rating')
    outfit = models.ForeignKey('Outfit', help_text='Outfit being rated')

    def __unicode__(self):
        return "{} -- {} -- ({})".format(self.user, self.score, self.outfit)

    # is_expired ... check for date_created + 2 min

