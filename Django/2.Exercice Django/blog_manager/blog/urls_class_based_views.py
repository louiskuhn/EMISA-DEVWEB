from django.urls import path
from .views_class_based_views import ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='liste_articles'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='detail_article'),
    path('ajouter/', ArticleCreateView.as_view(), name='ajouter_article'),
]
