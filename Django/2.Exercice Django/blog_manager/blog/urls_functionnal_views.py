from django.urls import path
from . import views_functionnal_views

urlpatterns = [
    path('', views_functionnal_views.liste_articles, name='liste_articles'),
    path('article/<slug:slug>/', views_functionnal_views.detail_article, name='detail_article'),
    path('ajouter/', views_functionnal_views.ajouter_article, name='ajouter_article'),
]

