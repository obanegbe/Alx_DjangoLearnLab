# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
from book_store.models import Book

new_book = Book.objects.get(title="1984")
new_book.title = "Nineteen Eighty-Four"
new_book.save()

# Expected output:
# The book's title is updated successfully in the database.
# >>> book.title
# 'Nineteen Eighty-Four'
