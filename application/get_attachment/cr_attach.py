from application.search_users.unload_d import UserIterate
from application.search_users.db import new_data
from application.search_users.db import get_last_userid
from application.get_attachment.t_photo import PhotoID
from application.get_attachment.s_photos import AtMessage
import logging



def get_attachment(token, token_vk, dict_for_search):

    logging.basicConfig(filename='myLogs', filemode='a', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.debug(f'Функция {get_attachment.__name__} зарегистрирована.')

    # Проверка наличия записей в БД
    last_userID = get_last_userid()
    if last_userID == None:
        last_userID = 0

    # Ищет кандидатов в вк

    logging.basicConfig(filename='myLogs', filemode='a', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.debug(f'Функция поиска запущена.')

    a = UserIterate(token, dict_for_search,last_userID)
    list_of_candidate = a.searching(token, dict_for_search,last_userID)
    print(list_of_candidate)

    logging.basicConfig(filename='myLogs', filemode='a', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.debug(f'Функция записи в БД запущена.')

    # Записывает в БД кандидатов
    b = new_data(list_of_candidate)

    logging.basicConfig(filename='myLogs', filemode='a', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.debug(f'Функция формирования вложений запущена.')

    # Ищет в вк ID фото, записывает в БД, формирует вложение в сообщение
    list_of_attachments = []
    for user in list_of_candidate:
        users_id = user['id']
        c = PhotoID(users_id, token_vk)
        url = c._get_photos(users_id, token_vk)
        d = AtMessage(token, url)
        attachment = d.get_photo_for_message(token, url)
        list_of_attachments.append([users_id, attachment])

    return list_of_attachments