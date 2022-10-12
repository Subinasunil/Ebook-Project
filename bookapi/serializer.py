from rest_framework.serializers import ModelSerializer
from bookapi.models import Books,Reviews
from django.contrib.auth.models import User
from rest_framework import serializers

class BookSerializer(ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"


class UserSeializer(ModelSerializer):
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "username",
                "email",
                "password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ReviewSerializer(ModelSerializer):
    book = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields= "__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        book=self.context.get("book")
        return Reviews.objects.create(user=user,book=book,**validated_data)