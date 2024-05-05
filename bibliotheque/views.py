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
        
        
        
class LivresView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Livres.objects.all()  
        
        serializers = LivresSerializer(result, many=True)  
        return Response({'status': 'success', "Livres":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = LivresSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class LivresParCategoriesView(generics.ListAPIView):
    serializer_class = LivresSerializer

    def get_queryset(self):
        categorie_id = self.kwargs['categorie_id']
        return Livres.objects.filter(categories__id=categorie_id)