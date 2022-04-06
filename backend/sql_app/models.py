from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Hanzi(Base):
    __tablename__ = "hanzi"

    id = Column(Integer, primary_key=True, autoincrement=True)
    characterId = Column(String(255), index=True)
    fileName = Column(String, default="")
    tone = Column(Integer, default=0)
    pinyin = Column(String, default="")
    title = Column(String, default="")
    date = Column(String, default="")
    creator = Column(String, default="")
    subject = Column(String, default="")
    publisher = Column(String, default="")
    type = Column(String, default="")
    description = Column(String, default="")
    contributor = Column(String, default="")
    format = Column(String, default="")
    source = Column(String, default="")
    rights = Column(String, default="")
    identifier = Column(String, default="")
    language = Column(String, default="chinese")
    relation = Column(String, default="")
    coverage = Column(String, default="")

