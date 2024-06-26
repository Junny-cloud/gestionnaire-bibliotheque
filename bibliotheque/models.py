from django.db import models
from django.utils.text import slugify 
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL
class Categories(models.Model):
     nom = models.CharField(max_length=200, null=True, unique=True,blank=True, verbose_name="Nom categorie")
     slug = models.SlugField(unique=True, null=True)
     
     date_registry = models.DateTimeField( auto_now_add=True,verbose_name="Date d'enregistrement")
     date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
     status = models.BooleanField(default=True, verbose_name='Etat')
     
     class Meta:
          verbose_name = "Categorie"
          verbose_name_plural = "Categories"
          ordering = ['-id']

     def __str__(self):
          return f"{self.id}"
     
     def save(self, *args, **kwargs):
        # Générer le slug à partir du nom de la catégorie avant de sauvegarder
        self.slug = slugify(self.nom)
        super(Categories, self).save(*args, **kwargs)
        

class Livres(models.Model):
     nom = models.CharField(max_length=200, null=True, blank=True)
     slug = models.SlugField(unique=True, null=True)
     categories = models.ManyToManyField(Categories, blank=False)
     description = models.TextField( null=True, blank=True)
     
     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="bibliothécaire")
     date_registry = models.DateTimeField( auto_now_add=True,verbose_name="Date d'enregistrement")
     date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
     status = models.BooleanField(default=True, verbose_name='Etat')
     
     class Meta:
          verbose_name = "Livre"
          verbose_name_plural = "Livres"
          ordering = ['-id']

     def __str__(self):
          return f"{self.nom}"
     
     def save(self, *args, **kwargs):
        # Générer le slug à partir du nom du livre avant de sauvegarder
        self.slug = slugify(self.nom)
        super(Livres, self).save(*args, **kwargs)
