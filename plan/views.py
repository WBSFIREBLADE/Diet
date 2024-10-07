from django.shortcuts import render
from .serializers import BookSerializers
from .models import Book
from rest_framework import viewsets


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

# Create your views here.
