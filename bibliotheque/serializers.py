from rest_framework import serializers
from bibliotheque.models import *
from users.models import *
import django_filters

class CategoriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)  
    def create(self, validated_data):  
         
        return Categories.objects.create(**validated_data)
    class Meta:
        model = Categories
        fields = ['name']
        
    
class BooksSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)  
    categories = CategoriesSerializer(many=True, read_only=True)
    description = serializers.CharField()
    
    def create(self, validated_data):  
         
        return Books.objects.create(**validated_data)
    class Meta:
        model = Books
        fields = ('name', 'categories', 'description')
     
        
class CustomUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):  
         
        return CustomUser.objects.create(**validated_data)
    class Meta:
        model = CustomUser
        fields = '__all__'
     
        
