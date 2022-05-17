import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    username = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    fav_character = Column(Integer, ForeignKey("character.id"))
    fav_planet = Column(Integer, ForeignKey("planet.id"))
    fav_vehicle = Column(Integer, ForeignKey("vehicle.id"))
    
    

class Characters(Base):

    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)

    name = Column(String(250))
    age = Column(Integer)
    gender = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    homeworld = Column(Integer, ForeignKey("planets.id"))
    vehicles = Column(Integer, ForeignKey("vehicles.id"))

class Planets(Base):

    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    name = Column(String(250))
    diameter = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    inhabitants = Column(Integer, ForeignKey("characters.id"))

class Vehicles(Base):

    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)

    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_credits = Column(Integer)
    owner = Column(Integer, ForeignKey("characters.id"))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')