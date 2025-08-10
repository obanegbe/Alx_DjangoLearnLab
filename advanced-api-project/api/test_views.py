from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2010)

        self.list_url = reverse("book-list")   # Make sure your urls.py names match
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})


    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)


    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)


    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized Book", "author": "No Auth", "publication_year": 2025}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Updated Title", "author": "Author One", "publication_year": 2001}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")


    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Author One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book Two")
