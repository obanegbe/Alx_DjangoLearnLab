import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found.")

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Book.objects.filter(library=library)
        print(f"\nBooks in library '{library.name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for '{library.name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to '{library_name}'.")

# Test the queries
if __name__ == "__main__":
    books_by_author("Chinua Achebe")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
