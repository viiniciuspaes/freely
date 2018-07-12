from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class HashTag(Base):
    __tablename__ = "hashtag"

    id = Column("id_hashtag", Integer, primary_key=True)
    name = Column("name", Text, nullable=False)


class Location(Base):
    __tablename__ = "location"

    id = Column("id_location", Integer, primary_key=True)
    name = Column("name",Text,nullable=False)
    latitude = Column("latitude", Text, nullable=False)
    longitude = Column("longitude", Text, nullable=False)


class Feeling(Base):
    __tablename__ = "feeling"

    id = Column("id_feeling", Integer, primary_key=True)
    name = Column("name", Text,  nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column("id_user", Integer, primary_key=True)
    id_location = Column("d_local", Integer, ForeignKey(Location.id))
    username = Column("username", Text, nullable=False)


class Font(Base):
    __tablename__ = "font"

    id = Column("id_font", Integer, primary_key=True)
    id_user = Column("id_user", Integer, ForeignKey(User.id))
    url = Column("url", Text)
    trust = Column("trust", Boolean)


class Tweet(Base):
    __tablename__ = "tweet"

    id = Column("id_tweet", Integer, primary_key=True)
    id_user = Column("id_user", Integer, ForeignKey(User.id), nullable=False)
    id_hashtag = Column("id_hashtag", Integer,ForeignKey(HashTag.id))
    id_location = Column("id_location", Integer, ForeignKey(Location.id),)
    id_feeling = Column("id_feeling", Integer, ForeignKey(Feeling.id))
    id_font = Column("id_font", Integer, ForeignKey(Font.id))
    text = Column("text_tweet", Text, nullable=False)
    n_reply = Column("n_reply", Integer)
    n_retweets = Column("n_retweets", Integer)
    n_likes = Column("n_likes", Integer)
    data = Column("data", DateTime)
    fake = Column("fake", Boolean)


class UserFeeling(Base):
    __tablename__ = "user_feeling"

    id = Column("id", Integer, primary_key=True)
    id_user = Column("id_user", Integer, ForeignKey(User.id), nullable=False)
    id_feeling = Column("id_feeling", Integer, ForeignKey(Feeling.id), nullable=False)


def get_engine():

    user = "root"
    password = ""
    address = "localhost"
    database_name = "freely"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)

    return engine


def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine)


def init(drop_tables=False):
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
    if drop_tables:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)
