from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# ==============================
# BookSerializer
# ==============================
# Purpose:
#   Serializes and deserializes Book instances into JSON and back.
# Fields:
#   - All model fields (title, publication_year, author).
# Custom Validation:
#   - Ensures that publication_year is not set in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom field-level validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# ==============================
# AuthorSerializer
# ==============================
# Purpose:
#   Serializes Author instances and includes related Book instances.
# Fields:
#   - name: Author's name.
#   - books: Nested list of books related to the author.
# Relationship Handling:
#   - Uses nested BookSerializer to serialize the related 'books' from the Author model.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to represent all books by this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
