import json

def get_token():
    with open('token+DSN.json', encoding='utf-8') as f:
        news = json.load(f)
        token = news['token']
        token_vk = news['token_vk']
        DSN = news['DSN']

    return token, token_vk, DSN

