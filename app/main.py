from db.db import SessionLocal
from db.crud import get_all_books

def main():
    db = SessionLocal()
    books = get_all_books(db)
    
    print("Список книг в базе:")
    for book in books:
        print(f"Книга: {book.title} | Описание: {book.description} | Цена: {book.price} | Категория: {book.category.title}")
    
    db.close()

if __name__ == "__main__":
    main()