import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))

class Personajes_props(Base):
    __tablename__ = 'Personajes_props'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    altura = Column(String(250))
    masa = Column(String(250))
    color_cabello = Column(String(250))
    piel = Column(String(250))
    ojos = Column(String(250))
    fecha_nacimiento = Column(String(250))
    genero = Column(String(250))
    creacion = Column(String(250))
    editado = Column(String(250))
    nombre = Column(String(250))
    mundo_origen = Column(String(250))
    personajes_id = Column(Integer, ForeignKey('Personajes.id'))
    Personajes = relationship(Personajes)

class Planetas(Base):
    __tablename__ = 'Planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))

class Planetas_props(Base):
    __tablename__ = 'Planetas_props'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    clima = Column(String(250))
    diametro = Column(String(250))
    gravedad = Column(String(250))
    nombre = Column(String(250))
    periodo_orbital = Column(String(250))
    poblacion = Column(String(250))
    residentes = Column(String(250))
    periodo_rotacion = Column(String(250))
    superficie_acuatica = Column(String(250))
    terreno = Column(String(250))
    planetas_id = Column(Integer, ForeignKey('Planetas.id'))
    Planetas = relationship(Planetas)
    
class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    id_usuario = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
   

    def to_dict(self):
        return {}

class Favoritos(Base):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    planetas_id = Column(Integer, ForeignKey('Planetas.id'))
    personajes_id = Column(Integer, ForeignKey('Personajes.id'))
    Planetas = relationship(Planetas)
    Personajes = relationship(Personajes)
    User = relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')