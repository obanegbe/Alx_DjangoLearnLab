from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_view = ('title', 'author', 'publication_year')
    list_filters = ('title', 'author')

admin.site.register(Book, BookAdmin)
