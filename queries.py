from library import book
from customers import customer
from transactions import transaction
from base import Session


session = Session()
books = session.query(book).all()

print("All books")

for book in books:
    print(f'Title: {book.title} Author: {book.author} Category: {book.category}')
print('')
