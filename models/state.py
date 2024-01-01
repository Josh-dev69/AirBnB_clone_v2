#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class that inherit the BaseModel
    and the Base ORM """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # If storage engine is not DBStorage, add the following code
    if models.storage.__class__.__name__ != 'DBStorage':
        @property
        def cities(self):
            """ Getter method for cities linked to the current State """
            city_list = []
            for city in models.storage.all(models.City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
    else:
        cities = relationship('City', backref='state', cascade='all')
