# Exercice 1 : Initialisation d’un dépôt et premier commit

1. Créez un dossier pour votre projet et initialisez un dépôt Git dans ce dossier.
2. Créez un fichier `README.md` avec une description de votre projet.
3. Ajoutez ce fichier à Git et validez le changement avec un commit.

# Exercice 2 : Travailler avec les branches

1. Créez une nouvelle branche appelée `dev` pour y développer une fonctionnalité.
2. Ajoutez une modification dans cette branche et validez-la.
3. Fusionnez cette branche dans la branche principale `main`.

# Exercice 3 : Résolution de conflits

1. Créez deux branches à partir de `main` : `dev1` et `dev2`.
2. Modifiez le même fichier dans les deux branches de manière conflictuelle (modifiez la même ligne).
3. Fusionnez `dev1` dans `main`, puis tentez de fusionner `dev2` (ce qui générera un conflit).
4. Résolvez manuellement le conflit et complétez la fusion.

# Exercice 4 : Gestion des branches avec `git rebase`

1. Créez un dépôt Git avec une branche `main` et une branche `feature`.
2. Faites des commits dans les deux branches.
3. Utilisez `git rebase` pour réappliquer les commits de la branche `feature` sur `main`, réorganisant ainsi l'historique.

# Exercice 5 : Sauvegarder un travail temporairement avec `git stash`

1. Modifiez un fichier dans votre projet sans le committer.
2. Utilisez `git stash` pour mettre de côté ces modifications.
3. Récupérez les modifications plus tard avec `git stash apply`.