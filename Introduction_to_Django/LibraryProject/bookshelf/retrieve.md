# Retrieve and display all attributes of the book you just created.
from book_store.models import Book

new_book = Book.objects.get(title="1984")
print(book.title, book.author, book.published_year)

# Expected output:
# 1984 George Orwell 1949
