from django.db import models

# ==============================
# Author Model
# ==============================
# Represents a book author.
# Fields:
#   - name: The full name of the author.
# Relationships:
#   - An Author can be linked to multiple Book instances (One-to-Many).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ==============================
# Book Model
# ==============================
# Represents a book in the system.
# Fields:
#   - title: Title of the book.
#   - publication_year: The year the book was published.
#   - author: Foreign key linking each book to its Author.
# Relationships:
#   - A Book belongs to one Author (Many-to-One).
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
