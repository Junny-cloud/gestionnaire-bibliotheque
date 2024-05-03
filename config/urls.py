from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bibliotheque.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('categories/', CategoriesView.as_view(), name='categorie'),
    path('livres/', BooksView.as_view(), name='livres'),
    path('livres-par-categorie/<int:categorie_id>/', BooksByCategoriesView.as_view(), name='livres-par-categorie'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

