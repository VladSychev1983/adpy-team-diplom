import yaml
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

with open('..\settings.yaml', 'r') as f:
    yaml_read = yaml.load(f, Loader=yaml.SafeLoader)
    token = yaml_read['vk']['token']
f.close()







