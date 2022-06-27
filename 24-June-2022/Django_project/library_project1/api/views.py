from rest_framework import generics
from rest_framework import generics
from library_project1.books.models import Book


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
