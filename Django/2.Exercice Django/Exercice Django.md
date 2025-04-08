# Exercice Django – Mini blog

L'objectif est de créer une petite application de blog où l'utilisateur peut :
- voir la liste des articles existants,
- consulter le détail d'un article (défini par son titre, son auteur, sa date de création et son contenu),
- ajouter un nouvel article via un formulaire.

Ce projet réutilise les notions suivantes : modèles (models), migrations, interface admin, vues, templates, formulaires, routage (urls)

## Étape 0
Créer un projet Django intitulé `blog_manager` et une application `blog`

## Étape 1
Définir le modèle `Article` sans oublier un champ pour la date (automatique) et la méthode `__str__`

## Étape 2
Générer et appliquer les migrations

## Étape 3
Enregistrer le modèle dans l'administration et créer un superutilisateur pour tester l'interface d'admin

## Étape 4
Créer le formulaire d'ajout d'un article

## Étape 5
Créer les vues `liste_articles`, `detail_article` et `ajouter_article` (des vues fonctionnelles dans un premier temps)

## Étape 6
Configurer les URLs et les inclure dans le projet

## Étape 7
Créer les templates
1. template de base
2. liste des articles
3. détail d'un article
4. ajouter un article

## Attendus minimum

- Suivre chaque étape
- Tester, modifier et explorer les fichiers
- Ajouter une 10aine d'articles, naviguer entre les vues

## Attendus conseillés

- Valider les champs (longueur minimale, etc.)
- Afficher des messages de confirmation (avec `messages`)
- Ajouter une pagination avec `Paginator`
- Ajouter un champ `slug` pour avoir des URLs lisibles
- Intégrer une authentification utilisateur

