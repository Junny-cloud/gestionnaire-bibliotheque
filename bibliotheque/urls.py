from django.urls import path
from .views import *


app_name="api"

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categorie'),
    path('livres/', LivresView.as_view(), name='livres'),
    path('livres-par-categorie/<int:categorie_id>', LivresParCategoriesView.as_view(), name='livres-par-categorie'),   
  
]

