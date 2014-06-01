from django import template
from datetime import date

from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='get_user_pic')
def get_user_pic(value, arg):
    user = User.objects.get(pk=arg)

    return user.profile.picture.url

@register.filter(name='get_user_name')
def get_user_name(value, arg):
    user = User.objects.get(pk=arg)

    return user.username