from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status ,generics 
from .models import *  
from .serializers import *  
# Create your views here.  
  
class CategoriesView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Categories.objects.all()  
        serializers = CategoriesSerializer(result, many=True)  
        return Response({'status': 'success', "categories":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = CategoriesSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class BooksView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Books.objects.all()  
        serializers = BooksSerializer(result, many=True)  
        return Response({'status': 'success', "Livres":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = BooksSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class BooksByCategoriesView(generics.ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        categorie_id = self.kwargs['categorie_id']
        return Books.objects.filter(categories__id=categorie_id)