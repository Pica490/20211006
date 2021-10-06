import requests

list_of_candidate = []

res = []

class UserIterate:
    def __init__(self, token, dict_for_search, last_userID):
        self.token = token
        self.dict_for_search = dict_for_search
        self.last_userID = last_userID


    def _get_users(self, list_id, token):


        URL = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': list_id,
            'access_token': token,
            'v': '5.130',
            'fields': 'city, bdate, sex, relation, photo_id'
            }
        res = requests.get(URL, params=params).json()

        return res['response']

    def _user_processing(self, res, list_of_candidate, dict_for_search):
        for record in res:
            a_var_relation = [1,5,6,0]

            if record.get('bdate') == None or record.get('city') == None or record.get('relation') == None or record.get('photo_id') == None:
                list_of_candidate

            else:
                if record['city']['title'] == dict_for_search['city'] and record['sex'] == dict_for_search['ssex'] and dict_for_search['city'] and record['bdate'][-3:] == dict_for_search['bdate'][-3:]:
                    if record['relation'] in a_var_relation:
                        list_of_candidate.append(record)

            return (list_of_candidate)
        return list_of_candidate

    def searching(self, token, dict_for_search, last_userID):
        list_of_candidate =[]

        id = last_userID + 1

        while len(list_of_candidate) < 3:
            list_id = ''
            n = 1000
            for id in range(id, n + id+1
                            ):
                list_id = list_id + ', ' + str(id)

            res = self._get_users(list_id, token)
            list_of_candidate = self._user_processing(res,list_of_candidate,dict_for_search)
            list_id = ''

        return(list_of_candidate)