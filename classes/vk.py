import vk_api
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from classes.models import Favorits, VK_ID, VK_Favorit
import requests
from pprint import pprint

class VK:
    def __init__(self,token,user_token,session) -> None:
        self.token = token
        self.user_token = user_token
        self.session = session

        vk_session = vk_api.VkApi(token=token)#токен
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
        
        self.headers = { 'Authorization': f'Bearer {user_token}' }
    
    def hello_message(self):
        #Посылаем в канал сообщение с информацией о работе бота.
        for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        msg = event.text.lower()#сообщение
                        id_vk = event.user_id#id пользователя который отправил сообщение
                        pattern = r"(\w+)\s(\w+)\s(\w+)"
                        msg_response = 'Для поиска людей введите '
                        msg_response += 'Город Пол Возраст '
                        msg_response += '(Пример: Москва Мужской 30)'
                        if val := re.match(pattern,msg):
                            (city,gender,age) = self._get_data(val,id_vk)
                            self.search_user(city,gender,age,id_vk)
                            msg_response = 'Запрос успешно обработан!'
                            self.send_message(msg_response,id_vk)
                        elif msg:
                            self.send_message(msg_response,id_vk)                         
                        else:
                            self.send_message(msg_response,id_vk)

    def send_message(self,msg,user_id):
           self.vk.messages.send(user_id=user_id, message=msg, random_id=0)

    def send_message_with_photo(self,result:dict,user_id):
        for key,value in result.items():
            msg = f'{value["first_name"]} {value["last_name"]}\n'
            photo = self.get_user_photo(key)
            attachment = 'photo' + str(key) + '_' + str(photo)
            self.vk.messages.send(user_id=user_id, message=msg, attachment=attachment, random_id=0)


    def search_user(self,city,gender,age,id_vk):
        #Делаем запрос на поиск пользователей.
        result = {}
        gender_int = None
        gender_int = 1 if gender.find("муж") == -1 else 2
        age_plus_year = int(age) + 1
        params = {'hometown': city, 'sex': gender_int, 'status': 1, 'sort': 0, 'count': 3, 'age_from':age, 'age_to': age_plus_year,'v': 5.199, 'p1':'v1','fields':'photo_200'}
        url = 'https://api.vk.com/method/users.search'
        response = requests.get(url, headers=self.headers, params=params)
        for idx in range(0,len(response.json()["response"]["items"])):
            result[response.json()["response"]["items"][idx]["id"]] =  {
                'photo_200': response.json()["response"]["items"][idx]["photo_200"],
                'last_name': response.json()["response"]["items"][idx]["last_name"],
                'first_name': response.json()["response"]["items"][idx]["first_name"]
            }
        self.send_message_with_photo(result,id_vk)

    def _get_data(self,user_query,id_vk):
        res_data = user_query.group()
        (city,gender,age) = res_data.split()
        return city,gender,age

    def get_user_photo(self,owner_id):
        params = {'owner_id': str(owner_id), 'album_id':'profile', 'count':'1', 'v': 5.199, 'p1':'v1', 'access_token':self.user_token}
        url = 'https://api.vk.com/method/photos.get'
        response = requests.get(url, headers=self.headers, params=params)
        photo = response.json()["response"]['items'][0]['id']
        return photo
    
    def get_send_found_users():
        pass
    
    def get_save_found_users():
        pass
    
    def get_users_from_favorite(self, id_vk, session):
         favorit_list = []
         idvk = session.query(VK_ID.id_user).filter(VK_ID.id_user_vk == id_vk)
         query = session.query(Favorits.id_favorit_vk).select_from(Favorits).\
             join(VK_Favorit, VK_Favorit.id_favorit_vk == Favorits.id_favorit).\
             filter(VK_Favorit.id_user_vk == idvk).all()
         for idfav in query:
             favorit_list.append(idfav[0])
         return favorit_list
    def send_users_from_favorite():
        pass
    def next_user():
        pass