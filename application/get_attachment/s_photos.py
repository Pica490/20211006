import requests

class AtMessage:
    def __init__(self, token, URL):
        self.token = token
        self.URL = URL
        self.get_photo_for_message(token, URL)

    def get_photo_for_message(self, token, URL):

        URL1 = 'https://api.vk.com/method/photos.getMessagesUploadServer'
        params = {
            'groip_id': '207317329',
            'access_token': token,
            'v':'5.130',
            }

        a = requests.get(URL1, params).json()
        upload_url = a['response']['upload_url']

        r = requests.get(URL)
        image_data = r.content
        r = requests.post(upload_url, files={'photo': ('test.jpg', image_data)}).json()
        params ={'photo': r['photo'], 'server': r['server'], 'hash': r['hash'], 'access_token': token, 'v':'5.130'}
        c = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto', params).json()
        d = "photo{}_{}".format(c['response'][0]['owner_id'], c['response'][0]['id'])

        print(d)
        return d






