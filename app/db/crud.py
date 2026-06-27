from sqlalchemy.orm import Session
from .models import Book, Category

def create_category(db: Session, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_all_books(db: Session):
    return db.query(Book).all()

def create_book(db: Session, title: str, description: str, price: float, category_id: int):
    book = Book(title=title, description=description, price=price, category_id=category_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book_price(db: Session, book_id: int, new_price: float):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.price = new_price
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

