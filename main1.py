from application.bot_message.w_message import Bot
from application.bot_message.get_token import get_token



if __name__ == "__main__":

    v = get_token()
    token = v[0]
    token_vk = v[1]

    bot = Bot(token, token_vk)
    user_id = bot.listen_bot(token, token_vk)




