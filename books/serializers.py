from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Book


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', ]


class BookSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'owner', 'title', 'description', 'image', ]
        