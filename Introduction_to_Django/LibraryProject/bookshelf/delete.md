# Delete the book you created and confirm the deletion by trying to retrieve all books again.
from book_store.models import Book
from bookshelf.models import Book

new_book = Book.objects.get(title="Nineteen Eighty-Four")
new_book.delete()

# Confirm deletion:
print(Book.objects.all())

# Expected output:
# QuerySet []  ← The book has been deleted; nothing remains in the table.
