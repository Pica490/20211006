import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from application.bot import User
import random
from application.get_attachment.cr_attach import get_attachment
from application.get_token import get_token

v = get_token()
token = v[0]
token_vk = v[1]

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

print("Server started"
      "")

def write_msg(user_id, message, attachment):

    vk.method('messages.send', {'user_id': user_id, 'message': message, "attachment": attachment, 'random_id': random.randrange(10 ** 7), })

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            print('New message:')
            print(f'For me by: {event.user_id}', end='')
            bot = User(event.user_id, token)

            if type(bot.new_message(event.text)) == list:
                print(bot.new_message(event.text))
                write_msg(event.user_id, bot.new_message(event.text)[0], None)
                list_of_attachments = get_attachment(token, token_vk, bot.new_message(event.text)[1])
                print(list_of_attachments)
                for attachment in list_of_attachments:
                    write_msg(event.user_id, f'Претендент https://vk.com/id{attachment[0]}', attachment[1])

            else:
                write_msg(event.user_id, bot.new_message(event.text), None)

            print('Text: ', event.text)


