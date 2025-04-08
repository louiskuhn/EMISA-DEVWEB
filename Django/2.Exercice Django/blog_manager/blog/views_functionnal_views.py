from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

def liste_articles(request):
    article_list = Article.objects.all().order_by('-date_creation')
    paginator = Paginator(article_list, 5)  # Affichage de 5 articles par page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/detail_article.html', {'article': article})

def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre article a été publié avec succès !")
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'blog/ajouter_article.html', {'form': form})

