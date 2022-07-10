from cgitb import lookup
from rest_framework import serializers
from .models import Books
from django.contrib.auth import get_user_model

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name', 'author', 'availability_status', 'borrower')
        lookup_field = 'id'


