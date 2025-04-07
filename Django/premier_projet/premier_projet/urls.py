from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salutation/', include('salutation.urls', namespace='salutation')),
    path('user/', include('utilisateur.urls', namespace='user')),
]
