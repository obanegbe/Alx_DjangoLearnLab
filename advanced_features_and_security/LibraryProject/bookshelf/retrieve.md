# Retrieve and display all attributes of the book you just created.
from bookshelf.models import Book

new_book = Book.objects.get(title="1984")
print(new_book.title, new_book.author, new_book.published_year)

# Expected output:
# 1984 George Orwell 1949

