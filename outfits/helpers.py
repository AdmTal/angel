import requests
from angel.settings import get_env_variable


# ignoring device option for now
def push_notification(user_key, title, message):
    """Send Push notification through Pushover.net's api"""
    url = 'https://api.pushover.net/1/messages.json'

    data = {
        'token': get_env_variable('PUSH_OVER_TOKEN'),
        'user': user_key,
        'title': title,
        'message': message,
    }

    return requests.post(url, data=data)