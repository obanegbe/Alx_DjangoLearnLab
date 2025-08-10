from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_view = ('title', 'author', 'code .publication_year')
    list_filter = ('genre', 'is_available')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
