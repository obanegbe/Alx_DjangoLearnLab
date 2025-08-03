from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path


# Initialize router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for BookList (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Routes for BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

