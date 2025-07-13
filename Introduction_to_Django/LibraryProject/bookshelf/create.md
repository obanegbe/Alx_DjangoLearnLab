# Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
from book_store.models import Book

new_book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)

# Expected output:
# A Book object is created successfully and saved to the database.
# Example (in shell):
# >>> book
# <Book: 1984>
