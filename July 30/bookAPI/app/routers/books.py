from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# Create a book
@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


# Get all books
@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


# Get a book by ID
@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# Update a book
@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int,
                updated_book: schemas.BookUpdate,
                db: Session = Depends(get_db)):

    book = crud.update_book(db, book_id, updated_book)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# Delete a book
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}

