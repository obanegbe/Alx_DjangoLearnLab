# urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

from django.urls import path
from .views import register_view, login_view, logout_view, list_books, LibraryDetailView

["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Auth routes
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
