from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions:
    list, create, retrieve, update, and destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


