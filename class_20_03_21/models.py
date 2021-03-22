from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
import os

DB_NAME = f'{os.getcwd()}/restaurant.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

class ScrapingService(Base):
    __tablename__ = 'scraping_service'
    service_id = Column(Integer, primary_key=True)
    name = Column(String)
    base_url = Column(String, unique=True)
    restaurants = relationship('Restaurant', backref=backref("scraping_service"))


class Restaurant(Base):
    __tablename__ = 'restaurant'
    restauran_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    open_hours = Column(String)
    image_url = Column(String)
    name_id = Column(String, unique=True, nullable=False)
    service_id = Column(Integer, ForeignKey('scraping_service.service_id'))

meta = Base.metadata

if __name__ == '__main__':
    meta.create_all(engine)
