from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from .forms import ArticleForm

# def salutation_home(request):
#     contexte ={
#         "user": "pierpoljak"
#     }
#     return render(request, "salutation/home.html", contexte)

class HomeView(TemplateView):
    template_name = "salutation/home.html"

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        contexte["user"] = "pierpoljak"
        return contexte
    
def bonjour(request):
    return render(request, "salutation/bonjour.html")

def au_revoir(request):
    return render(request, "salutation/au_revoir.html")

def ajouter_article(request):
    if request.method ==  "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salutation:home') # redirect(reverse('salutation:home')) après "from django.urls import reverse"

    else:
        form = ArticleForm()
        return render(request, "salutation/formulaire.html", {"form": form})
