import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    last_name = Column(String(120))
    username = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(80), nullable=False)
    image = Column(String(800))

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    synopsis = Column(String(200000))
    year = Column(Integer)
    time_line = Column(Integer)
    rating = Column(Float)
    image = Column(String(800))
    category = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(300))
    image = Column(String(800))
    news_description = Column(String(200000))
    writer = Column(String(200))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating_in_stars = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(10000))
    date_and_hour = Column(DateTime)
    reviews_id = Column(Integer, ForeignKey('reviews.id'))
    reviews = relationship(Reviews)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comments_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship(Comments)
    
class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    movies_id = Column(Integer, ForeignKey('movies.id'))
    movies = relationship(Movies)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
