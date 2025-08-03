from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions:
#     list, create, retrieve, update, and destroy
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users with a valid token can access
