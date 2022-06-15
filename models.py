from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer, default=0)
    section = Column(Integer, default=0)
