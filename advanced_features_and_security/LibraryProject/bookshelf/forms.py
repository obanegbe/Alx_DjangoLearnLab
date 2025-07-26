from django import forms
from .models import Book

["ExampleForm"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'is_available']
