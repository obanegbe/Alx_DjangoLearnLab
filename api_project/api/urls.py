from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for BookList (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Routes for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]
