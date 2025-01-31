#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.state import State
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', back_populates='city',
                              cascade='all, delete, delete-orphan')
        state = relationship('State', back_populates='cities')
    else:
        state_id = ""
        name = ""
