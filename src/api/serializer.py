from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):

    class Meta:
        model = Book
        field= ['name', 'auther', 'user', 'date',]