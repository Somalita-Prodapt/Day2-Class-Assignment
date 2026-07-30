from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Schema for creating a book
class BookCreate(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    status: Optional[str] = "available"


# Schema for updating a book
class BookUpdate(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    status: Optional[str] = "available"


# Schema for returning book data
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str]
    status: str
    added_at: datetime

    class Config:
        from_attributes = True

