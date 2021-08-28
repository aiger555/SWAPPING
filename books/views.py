from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import  get_object_or_404
from .models import Book
from .serializers import BookSerializer, UserSerializer

User = get_user_model()



class BookAPIView(APIView):
    
    permission_classes = [IsAuthenticated, ]
    
    def get(self, request):
        books = Book.objects.all()
        user = User.objects.filter(username=User.username)
    
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        user = request.user
        
        if serializer.is_valid():
            description = serializer._validated_data.get('description')
            image = serializer._validated_data.get('image')
            book = Book.objects.create(creator=user, 
                                       body=description, 
                                       image=image)
            serializer = BookSerializer(instance=book)
            return Response(serializer.data)
        
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class BookDetailAPIView(APIView):
    
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(instance=book)
        return Response(serializer.data)

    def put(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer= BookSerializer(instance = book, data = request.data)

        if serializer.is_valid():
            description = serializer.validated_data.get('description')
            image = serializer.validated_data.get('image')
            book.description = description
            book.image = image
            book.save()
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response({'detail':'success'}, status=status.HTTP_204_NO_CONTENT)