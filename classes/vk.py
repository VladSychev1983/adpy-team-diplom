import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

class VK:
    def __init__(self,token) -> None:
        self.token = token
        vk_session = vk_api.VkApi(token=token)#токен
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
    
    def hello_message(self):
        #send info msg to vk channel ask for age,gender,city 
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()#сообщение
                    id_vk = event.user_id#id пользователя который отправил сообщение
                    print(msg)
                    print(id_vk)
                    self.vk.messages.send(user_id=id_vk, message=msg, random_id=0)

    def search_user(self,age,gender,city):
        #do query to vk api for searching users .
        pass

