from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):
    """Extra information to track for each user"""
    user = models.OneToOneField(User, related_name='profile')

    picture = models.ImageField(upload_to='profile_images', blank=True, help_text='Your pretty face')

    pushover_key = models.CharField(max_length=256, help_text='account key from pushover')

    friends = models.ManyToManyField(User, blank=True, null=True, help_text='A trusted friend')

    def __unicode__(self):
        return str(self.user)