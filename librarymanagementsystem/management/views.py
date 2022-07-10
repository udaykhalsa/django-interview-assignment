from rest_framework.views import APIView
from rest_framework import viewsets, status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsLibrarian
from django.contrib.auth import get_user_model
from .models import Books
from .serializers import BookSerializer

User = get_user_model()


class ShowBooksBview(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class AddBookView(generics.CreateAPIView):
    queryset = Books.objects.all()
    model = Books
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class UpdateBookView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class RemoveBookView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)
