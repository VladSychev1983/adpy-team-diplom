import yaml
from yaml import load
import sqlalchemy
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy import insert
from classes.models import VK_Favorit,VK_ID,Favorits,create_tables,drop_tables

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from classes.vk import VK


def main():
    settings_dict = {}
    stream = open("settings.yaml", 'r',encoding="utf-8")
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
    
    #Далее работаем с классам VK получаем результаты и вызываем новые классы, записываем в базу.
    vk_token = str(settings_dict["vk"]["group_token"])
    vk_user_token = str(settings_dict["vk"]["user_token"])
    vk_obj = VK(vk_token,vk_user_token,session)
    vk_obj.hello_message()

    #session.add(VK_ID(id_user_vk=id_vk))
    #session.commit()

if __name__ == '__main__':
    main()