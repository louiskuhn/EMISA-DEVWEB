from django.urls import path
from . import views

app_name="salutation"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bonjour/', views.bonjour, name='bonjour'),
    path('au_revoir/', views.au_revoir, name='au_revoir'),
    path('formulaire/', views.ajouter_article, name='formulaire'),
]
