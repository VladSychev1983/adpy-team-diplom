import yaml
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

with open('..\settings.yaml', 'r') as f:
    yaml_read = yaml.load(f, Loader=yaml.SafeLoader)
    token = yaml_read['vk']['token']
f.close()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


class VK:
    def __init__(self, id_vk):
        self.id_vk = id_vk

    def get_data(self):
        user_info_get = vk.users.get(user_ids=self.id_vk, fields='sex, city, bdate')
        # sex 0 не указан, 1 жен, 2 муж
        date = user_info_get[0]['bdate']
        sex = user_info_get[0]['sex']
        city = user_info_get[0]['city']['title'] if 'city' in user_info_get[0] else None #Возвращет None, если не указан город
        return {'id': self.id_vk, 'date': date, 'sex': sex, 'city': city}






