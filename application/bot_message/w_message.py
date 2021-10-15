import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from application.bot_message.bot import User
from application.get_attachment.cr_attach import get_attachment

class Bot:
    def __init__(self, token, token_vk):
        self.token = token
        self.token_vk = token_vk
        self.vk = None
        self.user_id = None
        self.text = None

    def listen_bot(self, token, token_vk):

        self.vk = vk_api.VkApi(token=token)
        longpoll = VkLongPoll(self.vk)

        print("Server started"
          "")

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:

                    print('New message:')
                    print(f'For me by: {event.user_id}', end='')

                    self.user_id = event.user_id
                    self.text = event.text
                    bot = User(event.user_id, token)
                    self.cr_message(bot)

        return


    def cr_message(self, bot):

        if type(bot.new_message(self.text)) == list:
            print(bot.new_message(self.text))
            self.write_msg(self.user_id, bot.new_message(self.text)[0], None)
            list_of_attachments = get_attachment(self.token, self.token_vk, bot.new_message(self.text)[1])
            print(list_of_attachments)
            for attachment in list_of_attachments:
                self.write_msg(self.user_id, f'Претендент https://vk.com/id{attachment[0]}', attachment[1])

        else:
            self.write_msg(self.user_id, bot.new_message(self.text), None)

    def write_msg(self, user_id, message, attachment):
        vk = self.vk
        vk.method('messages.send', {'user_id': user_id, 'message': message, "attachment": attachment,
                                        'random_id': random.randrange(10 ** 7), })
