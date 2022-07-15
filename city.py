from sqlalchemy import Column, Integer, String, ForeignKey
from database import base


class City(base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    people_count = Column(Integer)
    url = Column(String)

    def __init__(self, name:str, count: int, url: str):
        self.name = name
        self.people_count = count
        self.url = url

    def __repr__(self):
        return {'Город': {self.name}, 'Численность': {self.people_count}, 'URL': {self.url}}
        #f'{self.name} {self.people_count}\n{self.url}'