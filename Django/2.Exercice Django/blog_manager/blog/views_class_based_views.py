from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/liste_articles_class_based_views.html'
    ordering = ['-date_creation']
    paginate_by = 5  # Affiche 5 articles par page et passe par défaut en contexte les variable page_obj et object_list à réutiliser dans le template 

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail_article.html'
    context_object_name = 'article'
    # Utilisation du slug pour trouver l'article dans l'URL
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/ajouter_article.html'
    success_url = reverse_lazy('liste_articles')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Votre article a été publié avec succès !")
        return response
