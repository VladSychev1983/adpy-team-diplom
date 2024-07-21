import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

from classes.models import Favorits, VK_ID, VK_Favorit


class VK:
    def __init__(self,token) -> None:
        self.token = token
        vk_session = vk_api.VkApi(token=token)#токен
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
    
    def hello_message(self):
        #send info msg to vk channel ask for age,gender,city 
        for event in self.longpoll.listen():
            try:
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        msg = event.text.lower()#сообщение
                        id_vk = event.user_id#id пользователя который отправил сообщение
                        if msg == 'начать':
                            return id_vk
                    else:    
                        self.vk.messages.send(user_id=id_vk, message=msg, random_id=0)
            except:
                self.vk.messages.send(user_id=id_vk, message='Неправильная команда', random_id=0)

    def search_user(self,age,gender,city):
        #do query to vk api for searching users .
        pass
    def get_data():
        pass
    def get_user_photo():
        pass
    def get_send_found_users():
        pass
    def get_save_found_users():
        pass
    def get_users_from_favorite(self, id_vk, session):
        favorit_list = []
        favorit_dict = []
        url = 'https://api.vk.com/method/users.get'
        param = {
            'access_token': self.token,
            'fields': 'id, first_name, last_name, photo_200_orig',
            'v': '5.199'
        }
        idvk = session.query(VK_ID.id_user).filter(VK_ID.id_user_vk == id_vk).all()[0][0]
        query = session.query(Favorits.id_favorit_vk).select_from(Favorits).\
            join(VK_Favorit, VK_Favorit.id_favorit_vk == Favorits.id_favorit).\
            filter(VK_Favorit.id_user_vk == idvk).all()
        for idfav in query:
            favorit_list.append(idfav[0])
        for id in favorit_list:
            responce = requests.get(url=url, params={**param, 'user_ids': str(id)})
            favorit_dict.append({
                'id': id,
                'link': f'https://vk.com/id{id}',
                'first_name': responce.json()['response'][0]['first_name'],
                'last_name': responce.json()['response'][0]['last_name'],
                'photo_url': responce.json()['response'][0]['photo_200_orig']
            })
        return favorit_dict
    def send_users_from_favorite():
        pass
    def next_user():
        pass
    