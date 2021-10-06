import requests
from application.search_users.db import add_data

class PhotoID:
    def __init__(self, users_id, token_vk):
        self.users_id = users_id
        self.token_vk = token_vk
        self._get_photos(users_id,token_vk)

    def _get_photos(self, users_id, token_vk):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
        'user_id': users_id,
        'access_token': token_vk,
        'v':'5.130',
        'album_id' : 'profile',
        'extended' : '-1'
        }
        res = (requests.get(URL, params=params)).json()

        d = {}

        if res['response']['count'] > 0:
            counter_likes = 0
            for values in res['response']['items']:
                if values['likes']['count'] > counter_likes:
                    counter_likes = values['likes']['count']
                    url = values['sizes'][0]['url']
                add_data(users_id, url)

        return url


