import yaml
from yaml import load
import sqlalchemy
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy import insert
from classes.models import VK_Favorit, VK_ID, Favorits, create_tables, drop_tables
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from classes.vk import VK

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from classes.vk import VK

if __name__ == '__main__':
    settings_dict = {}
    stream = open("settings.yaml", 'r', encoding="utf-8")
    settings_dict = yaml.load(stream, Loader)

    db_user = str(settings_dict["db"]["db_user"])
    db_pass = str(settings_dict["db"]["db_pass"])
    db_host = str(settings_dict["db"]["db_host"])
    db_port = str(settings_dict["db"]["db_port"])
    db_name = str(settings_dict["db"]["db_name"])

    DSN = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # father work with vk classes.
    vk_token = str(settings_dict["vk"]["token"])
    vk_session = vk_api.VkApi(token=vk_token)  # токен
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    vk_obj = VK(vk_token)

    def start_bot():
        for event in longpoll.listen():
            try:
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        msg = event.text.lower()
                        id_vk = event.user_id
                        if msg == 'начать':
                            try:
                                session.add(VK_ID(id_user_vk=id_vk))
                                session.commit()
                            except:
                                pass

                        else:
                            vk.messages.send(user_id=id_vk, message=msg, random_id=0)

            except:
                vk.messages.send(user_id=id_vk, message='Неправильная команда', random_id=0)

    start_bot()
