from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import BookSerializer
from .models import Book


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class= BookSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        return Book.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

# class 

    
