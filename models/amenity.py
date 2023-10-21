#!/usr/bin/python3
""" Amenity Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity """
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
