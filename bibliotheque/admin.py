from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from .models import *
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']
    list_filter = ['name']
    
    
class BooksAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'get_categories']
    list_filter = ['name']
    
    def get_categories(self, obj):
        return ", ".join([categorie.name for categorie in obj.categories.all()])
    
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Books, BooksAdmin)