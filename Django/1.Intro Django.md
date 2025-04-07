# Django : pas à pas

Des liens de cours complets et tops sur Django (c'est pas ça qui manque mais une petite sélection, en français siouplé):
- [djangogirls](https://tutorial.djangogirls.org/fr/)
- [python.doctor](https://python.doctor/page-django-introduction-python)
- [tresfacile.net](https://www.tresfacile.net/framework-django/)

## 1 Introduction à Django

### 1.1 Qu'est-ce que Django ?

Django est un **framework web** écrit en Python qui permet de **développer rapidement des applications web robustes et sécurisées**

Django est :
- un **framework "batteries-included"** : inclut tout ce qu'il faut (authentification, ORM, gestion des sessions…).  
- **basé sur l'architecture MVT** (**Modèle - Vue - Template**).  
- **sécurisé** : protection contre les failles courantes (CSRF, injection SQL, XSS…).  
- **rapide et efficace** : idéal pour les applications web évolutives.  

### 1.2 L'architecture MTV

Django suit le modèle MTV (Modèle-Template-Vue), une variante du modèle MVC (Modèle-Vue-Contrôleur) :

- **Modèle :** Gère les données de l'application (interactions avec la base de données).
- **Template :** Génère le rendu HTML à partir des données.
- **Vue :** Logique de traitement des requêtes utilisateur et liaison entre le Modèle et le Template.

## 1.3 Créer un projet Django

Un projet Django est un **ensemble d'applications** qui fonctionnent ensemble.  

Pour créer un nouveau projet :  
```sh
django-admin startproject nom_du_projet
```

### EXERCICE 1

1. Création de l'environnement de développement et installation de Django
   - Créer d'un environnement virtuel pour isoler les dépendances du projet.
   - Installer Django.

2. Création d'un premier son premier projet Django
   - Créer un projet `mon_premier_projet`.
   - Comprendre la structure des dossiers de base d'un projet Django
   
3. Démarrer le serveur de développement
   - Lancer le serveur avec `python manage.py runserver`.
   - Tester le projet Django localement sur `localhost` [http://127.0.0.1:8000/](http://127.0.0.1:8000/).



## 2 Création d'applications et gestion des vues

### 2.1 Création d'une application Django

Une **application** est une partie du projet ayant une fonctionnalité spécifique :
- La commande pour créer une application : `python manage.py startapp nom_application`.
- Structure d'une application : comprendre les fichiers principaux (`views.py`, `models.py`, `admin.py`).

### 2.2 Création d'une vue configuration des URLs

Une "vue" gère les requêtes HTTP et renvoie une réponse :
- Une vue est une fonction ou une classe qui traite les requêtes HTTP
- Créer une vue de base qui renvoie une réponse HTTP simple

### 2.3 Configuration des URLs

Le fichier `urls.py` permet de :
- Relier les vues aux URL
- Structurer les URL de l'application pour les organiser efficacement

### EXERCICE 2

1. Créer une application nommée `salutation` et comprendre la structure du dossier qui s'est créé
2. Dans cette application, définir une vue qui retourne « Bonjour, le monde ! » et configurer une URL pour y accéder
3. Ajouter une nouvelle vue `au_revoir` dans l'application `salutation` qui retourne "Au revoir !"
4. Configurer une URL pour accéder à cette vue
5. *Bonnes pratiques* : plutôt que de créer gérer les urls uniquement dans le fichier `premier_projet/urls.py`, on peut définir un fichier `salutation/urls.py` et ensuite "l'importer" dans `premier_projet/urls.py`


## 3 Les Templates dans Django

Les templates permettent d'afficher des pages HTML dynamiques.  

### 3.1 Introduction aux Templates Django

Les templates Django permettent d'injecter des données dynamiques dans le HTML
```html
<h1>Bonjour {{ nom_utilisateur }} !</h1>
```

Configurer les templates dans Django et les organiser dans un répertoire `templates`.

**Structure recommandée des dossiers de templates dans une application :**
Quand vous créez une app `appli`, vous devez organiser vos templates comme ceci :
```
appli/                      ← Dossier de l'application
├── templates/
│   └── appli/              ← Dossier de noms "namespaced" (nom de l'app)
│       └── home.html       ← Fichier HTML du template
```

Cela permet à Django de retrouver le bon template, même si d'autres apps ont aussi un `home.html`.


### 3.2 Utilisation des templates dans les vues

Rendre un template dans une vue avec la fonction `render`.  
```python
from django.shortcuts import render

def accueil(request):
    return render(request, 'appli/home.html')
```
Passer des données depuis la vue au template.  
```python
def accueil(request):
    contexte = {'nom_utilisateur': 'Alice'}
    return render(request, 'appli/home.html', contexte)
```
Et dans le template :
```html
<p>Bienvenue, {{ nom_utilisateur }} !</p>
```


### 3.3 Héritage de Templates

Créer un template de base pour une mise en page uniforme (comme vu dans Flask on utilise un template `base.html` avec les `{% block nom_bloc %}{% endblock %}` puis un `{% extends 'base.html' %}` dans les autres templates)
  

### EXERCICE 3

1. En utilisant toujours l'exemple `salutation`, créer un template de base avec un en-tête et un pied de page
2. Créer un template enfant qui affiche "Bienvenue dans les templates Django !"
3. Gérer la configuration des vues et des URLs 
4. Regarder du côté de `TemplateView` pour générer des vues de pages relativement simples


## 4 Les Modèles (Models) dans Django

Django embarque nativement un ORM pour créer des modèles et interagir facilement avec la base de données.

### 4.1 Création d'un modèle Django

Un modèle représente une **table dans la base de données**. Chaque attribut de classe devient une **colonne**.

Django ORM (Object Relational Mapping) permet de manipuler la base de données **avec du Python**, sans écrire une seule ligne de SQL.

On définit uniquement les champs de modèle et leurs types :
- `AutoField` : Un champ entier qui s'incrémente automatiquement.
- `BigAutoField` : Un entier sur 64 bits, similaire à `AutoField`, mais capable de contenir des nombres de 1 à 9223372036854775807.
- `BigIntegerField` : Un entier sur 64 bits, similaire à `IntegerField`, mais avec une plage garantie de -9223372036854775808 à 9223372036854775807.
- `BinaryField` : Un champ destiné au stockage de données binaires brutes.
- `BooleanField` : Un champ représentant une valeur vraie/fausse. Le widget de formulaire par défaut est une case à cocher (CheckboxInput).
- `CharField` : Un champ de texte conçu pour stocker de courtes chaînes de caractères.
- `DateTimeField` : Un champ représentant une date, avec une instance Python sous forme de datetime.date.
- `DecimalField` : Un champ pour les nombres décimaux à précision fixe, représentés par une instance Python de Decimal.
- `DurationField` : Un champ pour stocker des périodes de temps.
- `EmailField` : Un `CharField` vérifiant que la valeur est une adresse e-mail valide.
- `FileField` : Un champ pour télécharger des fichiers.
- `FloatField` : Un champ pour les nombres à virgule flottante, avec une instance Python sous forme de flottant.
- `ImageField` : Héritant de tous les attributs et méthodes de `FileField`, mais exigeant que l'objet téléchargé soit une image valide.
- `IntegerField` : Un champ pour les entiers, avec une plage sûre de -2147483648 à 2147483647 dans toutes les bases de données prises en charge par Django.
- `NullBooleanField` : Similaire à `BooleanField`, mais autorisant NULL comme option.
- `PositiveIntegerField` : Comme `IntegerField`, mais ne permettant que des valeurs positives ou nulles (0). La plage sûre est de 0 à 2147483647 dans toutes les bases de données prises en charge par Django.
- `SmallIntegerField` : Comme `IntegerField`, mais limité à des valeurs en dessous d'un certain point, dépendant de la base de données.
- `TextField` : Un champ de texte étendu. Le widget de formulaire par défaut est une zone de texte.
- `TimeField` : Un champ représentant l'heure, avec une instance Python sous forme de datetime.time.


```python
# appli/models.py

from django.db import models

class MaTable(models.Model):
    champ1 = models.IntegerField()
    champ2 = models.TextField()

    def __str__(self):
        return self.champ1
```



### 4.2 Migration de base de données

Une **migration** permet de créer ou modifier les tables dans la base de données à partir des modèles définis.

- Générer les fichiers de migration :
```bash
python manage.py makemigrations
```

- Appliquer les migrations (modifie la base) :
```bash
python manage.py migrate
```

Ces commandes créent automatiquement les tables en base de données à partir des classes Python.



### 4.3 Utilisation de l'interface d'administration Django

Django fournit une **interface d'administration** très pratique pour visualiser, créer, modifier et supprimer les données. Il faut

1. Créer un superutilisateur (avec un nom d'utilisateur, un e-mail, et un mot de passe) pour se connecter :
```bash
python manage.py createsuperuser
```

2. Accéder à l'admin :
Ouvrez [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

3. Enregistrer les modèles dans `admin.py` :
```python
# appli/admin.py

from django.contrib import admin
from .models import MaTable

admin.site.register(MaTable)
```

L'objet `Article` est maintenant visible et administrable dans le back office.



### EXERCICE 4

1. Créer un modèle `Article` avec les champs :
   - `titre` (champ texte court, max 100 caractères)
   - `contenu` (champ texte libre)
2. Générer les migrations et les appliquer.
3. Enregistrer le modèle dans l'administration Django.
4. Démarrer le serveur, accéder à l'interface d'admin, et créer quelques articles.



## 5 Les Formulaires dans Django

Django intègre un module `forms` pour gérer facilement les **entrées utilisateurs**, les valider et les enregistrer.


### 5.1 Création de Formulaires

Il existe deux façons principales :
- Les **formulaires classiques** (`forms.Form`)
- Les **ModelForms**, qui sont liés directement à un modèle (ils sont plus simple dans 90 % des cas)

Un exemple avec `ModelForm` :

```python
# appli/forms.py

from django import forms
from .models import MaTable

class MaTableForm(forms.ModelForm):
    class Meta:
        model = MaTable
        fields = ['champ1', 'champ2']
```

- `ModelForm` génère automatiquement les champs du formulaire à partir du modèle.
- Le formulaire est prêt à être utilisé dans une vue.


### 5.2 Gestion de la soumission de formulaires

Exemple d'une vue qui affiche le formulaire **et traite la soumission** :

```python
# appli/views.py

from django.shortcuts import render, redirect
from .forms import MaTableForm

def ajouter_observation(request):
    if request.method == 'POST':
        form = MaTableForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre en base
            return redirect('home')  # Redirige après soumission
    else:
        form = MaTableForm()

    return render(request, 'appli/ajouter_observation.html', {'form': form})
```

Et dans le template `ajouter_article.html` :

```html
<h2>Ajouter une observation dans MaTable</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enregistrer</button>
</form>
```

- `form.as_p` : affiche les champs du formulaire avec chaque champ entouré d'un paragraphe `<p>`
- `form.as_table` : affiche le formulaire sous forme de tableau HTML
- `form.as_ul` : chaque champ est dans une `<li>`
- le tag `{% csrf_token %}` protège contre les attaques CSRF


### EXERCICE 5

1. Créer un formulaire `ArticleForm` avec Django Forms (basé sur le modèle `Article`).
2. Créer une vue `ajouter_article` :
   - Si méthode GET : afficher le formulaire vide.
   - Si méthode POST : valider et enregistrer.
3. Créer un template avec un formulaire HTML.
4. Tester en ajoutant un article via cette page.



## 6 Authentification, Sessions, Utilisateurs et Permissions

Django fournit un système d'authentification complet pour gérer :
- l'enregistrement et la connexion des utilisateurs,
- les sessions utilisateurs,
- les permissions d'accès à certaines vues ou actions.

### 6.1 Utilisateurs et sessions

Django utilise un modèle `User` intégré dans `django.contrib.auth.models`.

Création d’un utilisateur dans l’administration :
```bash
python manage.py createsuperuser
```

Connexion à l’administration pour gérer les utilisateurs :
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Utiliser `request.user` dans une vue pour obtenir l’utilisateur connecté :
```python
def mon_profil(request):
    utilisateur = request.user
    return render(request, 'appli/profil.html', {'utilisateur': utilisateur})
```

### 6.2 Connexion / Déconnexion

Django inclut des vues toutes prêtes pour la connexion et la déconnexion.

Dans `urls.py` du projet :
```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='appli/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

Créer le template `login.html` :
```html
<h2>Connexion</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Se connecter</button>
</form>
```

> Après connexion, l’utilisateur est accessible via `request.user`  
> `request.user.is_authenticated` permet de savoir s’il est connecté

### 6.3 Restreindre l’accès à une vue

Restreindre l'accès à certaines vues avec le décorateur `login_required` :
```python
from django.contrib.auth.decorators import login_required

@login_required
def tableau_de_bord(request):
    return render(request, 'appli/dashboard.html')
```

### 6.4 Gestion des permissions

Chaque utilisateur peut avoir des **permissions** (droits spécifiques) ou être dans un **groupe**.

Restreindre l'accès à une vue à certains utilisateurs :
```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.view_article', raise_exception=True)
def vue_article_protegee(request):
    ...
```

Autres options utiles :
- `@user_passes_test(lambda u: u.is_superuser)`
- `@login_required` avec `LOGIN_URL` personnalisé dans `settings.py`

### EXERCICE 6

1. Ajouter les URLs de connexion et de déconnexion dans le fichier `urls.py` du projet.
2. Créer un template `login.html` pour la connexion.
3. Créer une vue `dashboard` accessible uniquement si l'utilisateur est connecté.
4. Créer un lien de déconnexion dans la barre de navigation (optionnelle).
5. BONUS : afficher dans la page d'accueil si l'utilisateur est connecté ou non (`{{ user.is_authenticated }}`).