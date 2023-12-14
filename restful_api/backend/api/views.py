from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListAPIView(generics.ListAPIView):
    '''API view for books list '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    '''API view for book creation '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveAPIView(generics.RetrieveAPIView):
    '''API view for book detail '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDestroyAPIView(generics.DestroyAPIView):
    '''API view for book delete '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    '''API view for book update '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
