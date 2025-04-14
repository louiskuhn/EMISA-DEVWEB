# Projet Django : Plateforme de gestion d'événements collaboratifs

Vous allez (si, si !) développer une **plateforme de gestion d'événements** permettant à des utilisateurs de s'inscrire, créer des événements, y participer, commenter, et gérer leurs activités.


## Fonctionnalités attendues

#### Authentification (Application `accounts`)
- Inscription avec email et mot de passe
- Connexion / déconnexion
- Profil utilisateur : afficher les événements créés et ceux auxquels il participe

#### Gestion des événements (Application `events`)
- Création / édition / suppression d'un événement
- Champs d'un événement : titre, description, date, lieu, capacité, image
- Liste publique des événements (avec pagination ou filtrage)
- Détail d'un événement
- S'inscrire / se désinscrire à un événement (si connecté)

#### Commentaires sur événements (Application `comments`)
- Commentaires visibles sur la page d'un événement
- Création/suppression de ses propres commentaires

#### Admin
- Interface Django admin avec personnalisation minimale
- Gestion des utilisateurs, événements, inscriptions et commentaires


## Contraintes techniques
- Évidemment utilisation du framework **Django**
- Architecture en **plusieurs applications**
- Utilisation du **système d'authentification Django** et des **sessions**
- Utilisation des **modèles relationnels** (OneToMany, ManyToMany)
- Templates avec `base.html` (héritage)
- Utilisation des **class-based views** (au minimum : `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
- Gestion des **permissions** (seuls les créateurs peuvent modifier/supprimer leurs événements)
- Bonus : filtres de recherche ou carte avec localisation des événements


## Suggestions

- Structurer le projet par étapes :

>1. authentification
>2. CRUD event
>3. inscriptions
>4. commentaires
>5. style

- Intégration possible de Bootstrap ou autre pour le front
- Ajout de tests unitaires (bonus)
- Git obligatoire

