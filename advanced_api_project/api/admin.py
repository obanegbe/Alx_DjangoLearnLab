from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book

# Register models so they can be managed via the Django admin site
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author')
