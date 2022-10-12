from django.shortcuts import render

from bookapi.models import Books,Reviews
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from bookapi.serializer import BookSerializer,UserSeializer,ReviewSerializer
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action

class UserModelView(ModelViewSet):
    serializer_class = UserSeializer
    queryset =User.objects.all()

class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Books.objects.filter(user=request.user)
        serializers=BookSerializer(qs,many=True)
        return Response(data=serializers.data)


    @action(methods=["post"], detail=True)
    def add_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        book = Books.objects.get(id=id)
        user = request.user
        serializer = ReviewSerializer(data=request.data, context={"user": user, "book": book})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["get"], detail=True)
    def get_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        book = Books.objects.get(id=id)
        reviews = book.reviews_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)




