# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Library, Book
from django.views.generic.detail import DetailView


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to show library detail and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('book_set__author')



# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Registration successful.')
            return redirect('list_books')  # Redirect to any view (like book list)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('list_books')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# User Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
