import vk_api
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from classes.models import Favorits, VK_ID, VK_Favorit

class VK:
    def __init__(self,token) -> None:
        self.token = token
        vk_session = vk_api.VkApi(token=token)#токен
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
    
    def hello_message(self):
        #Посылаем в канал сообщение с информацией о работе бота.
        for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        msg = event.text.lower()#сообщение
                        id_vk = event.user_id#id пользователя который отправил сообщение
                        pattern = r"(\w+)\s(\w+)\s(\w+)"
                        if val := re.match(pattern,msg):
                            self._get_data(val,id_vk)
                            msg_response = 'Запрос успешно обрабатывается!'
                            self.vk.messages.send(user_id=id_vk, message=msg_response, random_id=0)
                        elif msg:
                            msg_response = 'Для поиска людей введите '
                            msg_response += 'Город Пол Возраст '
                            msg_response += '(Пример: Москва Мужской 30)'
                            #msg_response = 'Для поиска людей введите Город Пол Возраст (Пример: Москва Мужской 30)'
                            self.vk.messages.send(user_id=id_vk, message=msg_response, random_id=0)                          
                        else:
                            msg_response = 'Для поиска людей введите'
                            msg_response += 'Город Пол Возраст'
                            msg_response += '(Пример: Москва Мужской 30)'  
                            self.vk.messages.send(user_id=id_vk, message=msg_response, random_id=0)            

    def search_user(self,city,gender,age):
        #do query to vk api for searching users .
        pass

    def _get_data(self,user_query,id_vk):
        res_data = user_query.group()
        (city,gender,age) = res_data.split()
        print(city,gender,age,id_vk)
        #сохраняем запрошенные данные в БД далее.?
        return city,gender,age,id_vk

    def get_user_photo():
        pass
    
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