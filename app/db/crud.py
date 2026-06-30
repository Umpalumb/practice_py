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

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, description: str, price: float, category_id: int):
    book = Book(title=title, description=description, price=price, category_id=category_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, update_data: dict):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        for key, value in update_data:
            if hasattr(book, key):
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

def get_all_categories(db: Session):
    return db.query(Category).all()

def update_category(db: Session, category_id: int, new_title: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category

