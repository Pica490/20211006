from application.search_users.db import delete_data
import requests


class User:
    def __init__(self, user_id, token):
        print("Создан объект бота!")
        self._dict_for_answer = {'appeal':["ПРИВЕТ", "ПОКА", "СЛЕДУЮЩИЕ"], 'relation':'', 'data':''}
        self.token = token
        self._USER_ID = user_id
        self._USERNAME = None
        self._USERPARAMS = self._get_user_PARAMS_from_vk_id(user_id, token)
        self.dict_for_search = self._get_param_for_search(self._USERPARAMS)

    def _get_user_PARAMS_from_vk_id(self, user_id, token):
        URL = 'https://api.vk.com/method/users.get'
        params = {
            'user_id': user_id,
            'access_token': token,
            'v': '5.130',
            'fields': 'city, bdate, sex, relation'
        }
        dict_user_params = requests.get(URL, params=params).json()
        self._USERNAME = dict_user_params['response'][0]['first_name']
        self._user_relation_check(dict_user_params)
        return dict_user_params

    #Проверка женат/замужем ли пользователь, внесение данных в словарь ответов
    def _user_relation_check(self, dict_user_params):
        if dict_user_params['response'][0]['relation'] == 1:
            self._user_full_data_check(dict_user_params)
        else:
            self._dict_for_answer['relation'] = 1

    # Проверка наличия в профиле данных для поиска, заплонение словаря
    def _user_full_data_check(self, dict_user_params):
        if dict_user_params['response'][0]['sex'] == '' or dict_user_params['response'][0]['sex'] == 0 or \
                dict_user_params['response'][0]['bdate'] == '' or dict_user_params['response'][0]['city'] == '':
            self._dict_for_answer['data'] = 1
            return self._dict_for_answer

    # Формирование словаря с параметрами пользователя
    def _get_param_for_search(self, param):

        if param['response'][0]['sex'] == 1:
            self.dict_for_search = {'city': param['response'][0]['city']['title'],
                                   'bdate': param['response'][0]['bdate'], 'ssex':2}
        else:
            self.dict_for_search = {'city': param['response'][0]['city']['title'],
                                   'bdate': param['response'][0]['bdate'], 'ssex':1}
        return self.dict_for_search


    def new_message(self, message):

        # Привет
        if message.upper() == self._dict_for_answer['appeal'][0] and self._dict_for_answer['relation']=='' and self._dict_for_answer['data'] =='':

            message = f"Привет-привет, {self._USERNAME}! Немного подожди!"

            return [message, self.dict_for_search]

        # Следующие
        elif message.upper() == self._dict_for_answer['appeal'][2]:

            message = f"Немного подожди, {self._USERNAME}!"

            return [message, self.dict_for_search]

        # Пока
        elif message.upper() == self._dict_for_answer['appeal'][1]:
            #Очищает БД
            delete_data()

            return f"Пока-пока, {self._USERNAME}!"

        # Женат/замужем
        elif message.upper() == self._dict_for_answer['appeal'][0] and self._dict_for_answer['relation'] == 1:

            return f"Привет, {self._USERNAME}, мы не разрушаем семьи!"

        # Заполни профиль
        elif message.upper() == self._dict_for_answer['appeal'][0] and self._dict_for_answer['data'] == 1 :
            return f"Привет,{self._USERNAME}, заполни в профиле город, дату рождения, пол!"

        else:
            return "Не понимаю о чем вы..."




