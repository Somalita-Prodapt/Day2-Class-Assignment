from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    status = Column(String, default="available")
    added_at = Column(DateTime, default=datetime.utcnow)

