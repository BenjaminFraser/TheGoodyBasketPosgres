#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
 
Base = declarative_base()

# User table column for the database
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    user_bio = Column(String(250))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'name'       : self.name,
           'email'      : self.email,
       }

# Create a Category column for the database
class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'      : self.user_id
       }
 
 # Create a category item column for the database
class CategoryItem(Base):
    __tablename__ = 'category_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    picture = Column(String(300))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'user_id'         : self.user_id,
           'category_id'         : self.category_id
       }



#engine = create_engine('postgresql://catalog:@52.36.82.174/thegoodybasket.db')
engine = create_engine('postgresql:///thegoodybasket')
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
