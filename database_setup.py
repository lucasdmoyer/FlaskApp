import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable = False)

	@property
	def serialize(self):
		return {
		'name':self.name,
		}

class Item(Base):
	__tablename__ = 'item'
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	price = Column(String(8))
	dateAdded = Column(Date)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
		'name': self.name,
		'description': self.description,
		'price': self.price,
		}

engine = create_engine('sqlite:///itemcatalogwithusers.db')

Base.metadata.create_all(engine)