from rest_framework import serializers
from bibliotheque.models import *
from users.models import *


class CategoriesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=200)  
    def create(self, validated_data):  
         
        return Categories.objects.create(**validated_data)
    class Meta:
        model = Categories
        fields = ('id','nom' )
        
    
class LivresSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(max_length=200, required=True)  
    categories = CategoriesSerializer(read_only=True,many=True)
    description = serializers.CharField()
    
    def create(self, validated_data):  
        categories = self.initial_data['categories']
        
        categoriesInstances = []
        
        for categorie in categories:
            categoriesInstances.append(Categories.objects.get(pk = categorie['id']))
        livres = Livres.objects.create(**validated_data)
        livres.categories.set(categoriesInstances)
        
        return livres
    class Meta:
        model = Livres
        fields = ('nom', 'categories', 'description')
     

     
        
