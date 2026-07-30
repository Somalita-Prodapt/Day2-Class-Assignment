from sqlalchemy.orm import Session

import models
import schemas


# Create a new book
def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        status=book.status
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# Get all books
def get_books(db: Session):
    return db.query(models.Book).all()


# Get a single book by ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


# Update a book
def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if existing_book:
        existing_book.title = book.title
        existing_book.author = book.author
        existing_book.genre = book.genre
        existing_book.status = book.status

        db.commit()
        db.refresh(existing_book)

    return existing_book


# Delete a book
def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

    return book

