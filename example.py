import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token='')#токен
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()#сообщение
            id_vk = event.user_id#id пользователя который отправил сообщение         
            vk.messages.send(user_id=id_vk, message=msg, random_id=0)
