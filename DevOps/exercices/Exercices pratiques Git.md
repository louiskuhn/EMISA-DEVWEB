# Exercice 1 : Initialisation d’un dépôt et premier commit

1. Créez un dossier pour votre projet et initialisez un dépôt Git dans ce dossier.
2. Créez un fichier `README.md` avec une description de votre projet.
3. Ajoutez ce fichier à Git et validez le changement avec un commit.

>### Solution :
>
>1. Création du dossier et initialisation de Git
>    ```bash
>    mkdir mon_projet
>    cd mon_projet
>    git init
>    ```
>
>2. Création du fichier `README.md`
>    ```bash
>    echo "blablabla" > README.md
>    ```
>
>3. Ajout du fichier à Git et commit :
>    ```bash
>    git add README.md
>    git commit -m "Ajout du fichier README"
>    ```

# Exercice 2 : Travailler avec les branches

1. Créez une nouvelle branche appelée `dev` pour y développer une fonctionnalité.
2. Ajoutez une modification dans cette branche et validez-la.
3. Fusionnez cette branche dans la branche principale `main`.

>#### Solution :
>1. Création nouvelle branche `dev` :
>     ```bash
>     git branch dev
>     git checkout dev
>     ```
>     OU
>     ```bash
>     git checkout -b dev
>     ```
>
>2. Ajout fonctionnalité dans la branche `dev` :
>     ```bash
>     echo "Nouvelle fonctionnalité" > fonctionnalite.txt
>     git add fonctionnalite.txt
>     git commit -m "Ajout de la nouvelle fonctionnalité"
>     ```
>
>3. Fusion branche `dev` avec `main` :
>     ```bash
>     git checkout main
>     git merge dev
>     ```
>
>VOir l'historique des branches et des commits
>     ```bash
>     git log --oneline --graph
>     ```

# Exercice 3 : Résolution de conflits

1. Créez deux branches à partir de `main` : `dev1` et `dev2`.
2. Modifiez le même fichier dans les deux branches de manière conflictuelle (modifiez la même ligne).
3. Fusionnez `dev1` dans `main`, puis tentez de fusionner `dev2` (ce qui générera un conflit).
4. Résolvez manuellement le conflit et complétez la fusion.

>#### Solution :
>1. Création branches à partir de `main` :
>     ```bash
>     # Branche 1
>     git checkout -b dev1
>     echo "Contenu de la branche dev1" > fichier.txt
>     git add fichier.txt
>     git commit -m "Modification sur dev1"
>
>     # Branche 2
>     git checkout main
>     git checkout -b dev2
>     echo "Contenu de la branche dev2" > fichier.txt
>     git add fichier.txt
>     git commit -m "Modification sur dev2"
>     ```
>
>2. Fusion `dev1` dans `main` :
>     ```bash
>     git checkout main
>     git merge dev1
>     ```
>
>3. Fusion `dev2` dans `main` (=> conflit) :
>     ```bash
>     git merge dev2
>     ```
>
>4. Résolution manuelle du conflit :
>   - Ouvrir et modifier le fichier en conflit
>   - Ajouter le fichier résolu à l'index et terminer la fusion :
>     ```bash
>     git add fichier.txt
>     git commit -m "Résolution du conflit entre dev1 et dev2"
>     ```

# Exercice 4 : Gestion des branches avec `git rebase`

1. Créez un dépôt Git avec une branche `main` et une branche `feature`.
2. Faites des commits dans les deux branches.
3. Utilisez `git rebase` pour réappliquer les commits de la branche `feature` sur `main`, réorganisant ainsi l'historique.

>#### Solution :
>1. Création dépôt et commit sur `main` :
>     ```bash
>     mkdir projet_rebase
>     cd projet_rebase
>     git init
>     echo "Version initiale" > fichier.txt
>     git add fichier.txt
>     git commit -m "Commit initial sur main"
>     ```
>
>2. Commits dans les 2 branches
>- Création branche `feature` et commit :
>     ```bash
>     git checkout -b feature
>     echo "Ajout d'une fonctionnalité" >> fichier.txt
>     git add fichier.txt
>     git commit -m "Commit sur la branche feature"
>     ```
>
>- Retour sur `main` et nouveau commit :
>     ```bash
>     git checkout main
>     echo "Amélioration sur main" >> fichier.txt
>     git add fichier.txt
>     git commit -m "Commit d'amélioration sur main"
>     ```
>
>3. Utilisation de `git rebase`
>- Faire un rebase de la branche `feature` sur `main` :
>     ```bash
>     git checkout feature
>     git rebase main
>     ```
>
>- Résoudre les conflits (si nécessaire) et terminer le rebase :
>     ```bash
>     git add fichier.txt
>     git rebase --continue
>     ```
>
>- Vérifiez l'historique :
>     ```bash
>     git log --oneline --graph
>     ```

# Exercice 5 : Sauvegarder un travail temporairement avec `git stash`

1. Modifiez un fichier dans votre projet sans le committer.
2. Utilisez `git stash` pour mettre de côté ces modifications.
3. Récupérez les modifications plus tard avec `git stash apply`.

>#### Solution :
>1. Modifier un fichier sans le committer :
>     ```bash
>     echo "Travail en cours" > fichier_temp.txt
>     ```
>
>2. Utiliser `git stash` pour sauvegarder temporairement ces modifications :
>     ```bash
>     git stash
>     ```
>
>3. Appliquer les modifications sauvegardées plus tard :
>     ```bash
>     git stash apply
>     ```
>
>4. Vérifier les stashes (optionnel) :
>     ```bash
>     git stash list
>     ```
