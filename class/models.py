import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()



class TG(Base):
    __tablename__ = 'tg'

    id_tg = sq.Column(sq.Integer, primary_key=True)
    id_user_tg = sq.Column(sq.BigInteger,  nullable=False)

class Favorits(Base):
    __tablename__ = 'favorits'
    id_favorit = sq.Column(sq.Integer, primary_key=True)
    id_vk = sq.Column(sq.Integer, nullable=False)


class TG_Favorit(Base):
    __tablename__ = 'TG_Favorit'
    id_tg_user = sq.Column(sq.Integer, sq.ForeignKey('tg.id_tg'), primary_key=True)
    id_vk_user = sq.Column(sq.Integer, sq.ForeignKey('favorits.id_favorit'), primary_key=True)

    id_tg = relationship(TG, backref='tg')
    id_vk = relationship(Favorits, backref='favorits')



def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables(engine):
    Base.metadata.drop_all(engine)