# **Introduction à Django**

#### **Module 1 : Introduction**
- **Objectif :** Comprendre ce qu'est Django, son architecture et comment il s'intègre dans le développement web.

1. **Qu'est-ce que Django ?**
   - Django est un framework web en Python conçu pour faciliter le développement rapide d'applications web sécurisées et maintenables. Django suit le modèle MTV (Modèle-Template-Vue), une variante du modèle MVC (Modèle-Vue-Contrôleur).
   - L'architecture MTV :
     - **Modèle :** Gère les données de l'application (interactions avec la base de données).
     - **Template :** Génère le rendu HTML à partir des données.
     - **Vue :** Logique de traitement des requêtes utilisateur et liaison entre le Modèle et le Template.

2. **Installation de Django et création de l’environnement de développement**
   - Installation de Python et Django.
   - Création d'un environnement virtuel pour isoler les dépendances du projet.

3. **Créer son premier projet Django**
   - Commande pour démarrer un projet : `django-admin startproject nom_du_projet`.
   - Comprendre la structure des dossiers de base d’un projet Django :
     - **manage.py** : fichier principal pour les commandes.
     - **settings.py** : fichier de configuration.
     - **urls.py** : gestion des URL.
     - **wsgi.py et asgi.py** : pour le déploiement.

4. **Démarrer le serveur de développement**
   - Lancer le serveur avec `python manage.py runserver`.
   - Tester le projet Django localement sur `localhost`.

**Exercice :**
1. Installer Django et démarrer un nouveau projet nommé `mon_premier_projet`.
2. Démarrer le serveur de développement et vérifier que la page de bienvenue Django s’affiche.

**Solution :**
```bash
# Étape 1 : Installer Django
pip install django

# Étape 2 : Créer un nouveau projet
django-admin startproject mon_premier_projet

# Étape 3 : Lancer le serveur dans le répertoire du projet
cd mon_premier_projet
python manage.py runserver
```



#### **Module 2 : Création d’applications et gestion des vues**
- **Objectif :** Créer des applications dans un projet Django, configurer des vues et définir des URL.

1. **Créer une application Django**
   - La commande pour créer une application : `python manage.py startapp nom_application`.
   - Structure d'une application : comprendre les fichiers principaux (`views.py`, `models.py`, `admin.py`).

2. **Configuration des vues**
   - Introduction aux vues dans Django. Une vue est une fonction ou une classe qui traite les requêtes HTTP.
   - Créer une vue de base qui renvoie une réponse HTTP simple.

3. **Configuration des URL**
   - Relier les vues aux URL dans Django en utilisant `urls.py`.
   - Structurer les URL de l'application pour les organiser efficacement.

**Exercice :**
1. Créer une application nommée `salutation`.
2. Dans cette application, définir une vue qui retourne « Bonjour, le monde ! » et configurer une URL pour y accéder.

**Solution :**
1. Créer l'application :
   ```bash
   python manage.py startapp salutation
   ```

2. Dans `salutation/views.py`, ajouter la vue suivante :
   ```python
   from django.http import HttpResponse

   def bonjour_vue(request):
       return HttpResponse("Bonjour, le monde !")
   ```

3. Dans `mon_premier_projet/urls.py`, configurer l’URL :
   ```python
   from django.urls import path
   from salutation import views

   urlpatterns = [
       path('bonjour/', views.bonjour_vue),
   ]
   ```

**Exercice supplémentaire :**
1. Ajouter une nouvelle vue `au_revoir_vue` dans l'application `salutation` qui retourne "Au revoir !".
2. Configurer une URL pour accéder à cette vue.

**Solution supplémentaire :**
1. Dans `salutation/views.py`, ajouter :
   ```python
   def au_revoir_vue(request):
       return HttpResponse("Au revoir !")
   ```

2. Dans `mon_premier_projet/urls.py`, ajouter :
   ```python
   path('au_revoir/', views.au_revoir_vue),
   ```



#### **Module 3 : Les Templates dans Django**
- **Objectif :** Utiliser des templates HTML pour afficher dynamiquement du contenu.

1. **Introduction aux Templates Django**
   - Les templates Django permettent d'injecter des données dynamiques dans le HTML.
   - Configurer les templates dans Django et les organiser dans un répertoire `templates`.

2. **Utilisation des templates dans les vues**
   - Rendre un template dans une vue avec la fonction `render`.
   - Passer des données depuis la vue au template.

3. **Héritage de Templates**
   - Créer un template de base pour une mise en page uniforme.
   - Étendre ce template de base dans les autres pages.

**Exercice :**
1. Créer un template de base avec un en-tête et un pied de page.
2. Créer un template enfant qui affiche "Bienvenue dans les templates Django !".

**Solution :**
1. Dans `salutation/templates/salutation/base.html` :
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}Mon Site{% endblock %}</title>
   </head>
   <body>
       <header><h1>Mon site Django</h1></header>
       {% block content %}{% endblock %}
       <footer><p>Texte de pied de page</p></footer>
   </body>
   </html>
   ```

2. Dans `salutation/templates/salutation/bienvenue.html` :
   ```html
   {% extends "salutation/base.html" %}
   {% block content %}
   <h2>Bienvenue dans les templates Django !</h2>
   {% endblock %}
   ```

3. Dans `salutation/views.py` :
   ```python
   from django.shortcuts import render

   def bienvenue_vue(request):
       return render(request, 'salutation/bienvenue.html')
   ```

4. Configurer l'URL dans `mon_premier_projet/urls.py` :
   ```python
   path('bienvenue/', views.bienvenue_vue),
   ```



#### **Module 4 : Les Modèles (Models) dans Django**
- **Objectif :** Créer des modèles pour interagir avec la base de données.

1. **Création des Modèles**
   - Comprendre le rôle de Django ORM (Object Relational Mapping) et créer des modèles de données.
   - Définir les champs de modèle et leurs types (CharField, IntegerField, DateField, etc.).

2. **Migration de base de données**
   - Générer et appliquer des migrations avec les commandes `makemigrations` et `migrate`.

3. **Utilisation de l’interface d’administration Django**
   - Accéder à l'interface d’administration pour gérer les données.
   - Enregistrer les modèles dans `admin.py` pour les rendre disponibles dans l’administration.

**Exercice :**
1. Créer un modèle `Article` avec les champs `titre` (champ de texte court) et `contenu` (champ de texte).
2. Enregistrer le modèle dans l'interface d'administration et créer des articles via cette interface.

**Solution :**
1. Dans `salutation/models.py` :
   ```python
   from django.db import models

   class Article(models.Model):
       titre = models.CharField(max_length=100)
       contenu = models.TextField()

       def __str__(self):
           return self.titre
   ```

2. Enregistrer le modèle dans `salutation/admin.py` :
   ```python
   from django.contrib import admin
   from .models import Article

   admin.site.register(Article)
   ```

3. Générer et appliquer les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Créer un superutilisateur pour accéder à l'administration :
   ```bash
   python manage.py createsuperuser
   ```



#### **Module 5 : Les Formulaires dans Django**
- **Objectif :** Gérer les entrées utilisateur avec les formulaires Django.

1. **Création de Formulaires**
   - Utiliser le module `forms` pour créer des formulaires basés sur les modèles.

2. **Gestion de la soumission de formulaires**
   - Traiter la soumission de formulaires dans les vues.

**Exercice :**
1. Créer un formulaire pour ajouter un nouvel `Article`.
2. Configurer une vue pour gérer la soumission du formulaire.

**Solution :**
1. Dans `salutation/forms.py`, créer le formulaire :
   ```python
   from django import forms
   from .models import Article

   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields = ['titre', 'contenu']
   ```

2. Dans `salutation/views.py`, créer la vue :
   ```python
   def ajouter_article_vue(request):
       if request.method == "POST":
           form = ArticleForm(request.POST)
           if

 form.is_valid():
               form.save()
               return HttpResponse("Article ajouté avec succès !")
       else:
           form = ArticleForm()
       return render(request, 'salutation/ajouter_article.html', {'form': form})
   ```

3. Créer le template `ajouter_article.html` :
   ```html
   <h2>Ajouter un nouvel article</h2>
   <form method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Soumettre</button>
   </form>
   ```

4. Ajouter l'URL dans `mon_premier_projet/urls.py` :
   ```python
   path('ajouter_article/', views.ajouter_article_vue),
   ```



#### **Module 6 : Conclusion et étapes suivantes**
- **Objectif :** Synthétiser les concepts vus et introduire des sujets avancés.

1. **Récapitulatif**
   - Passer en revue les concepts : applications, vues, modèles, templates, formulaires.

2. **Étapes suivantes**
   - Introduction à des sujets avancés : authentification, déploiement, développement d'API REST.

Chaque module de ce cours introduit progressivement les concepts et s’accompagne d’exercices pour consolider l’apprentissage.
