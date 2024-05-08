from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from .models import *
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'nom']
    list_filter = ['nom']
    
    
class LivresAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'nom', 'get_categories', 'user']
    list_filter = ['nom']
    
    def get_categories(self, obj):
        return ", ".join([categorie.nom for categorie in obj.categories.all()])
    
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Livres, LivresAdmin)