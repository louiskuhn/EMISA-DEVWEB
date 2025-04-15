from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Gestion de la connexion/déconnexion
    path('events/', include('events.urls')),
    path('comments/', include('comments.urls')),
    path('', include('events.urls')),  # La page d'accueil affiche la liste des événements
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)