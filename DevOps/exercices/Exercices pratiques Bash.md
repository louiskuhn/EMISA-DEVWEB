# Exercice 1 : Navigation et manipulation de fichiers

1. Créez un dossier nommé devops_bash
2. À l'intérieur de ce dossier, créez trois fichiers : app.py, requirements.txt, README.md
3. Copiez le fichier app.py et nommez la copie app_backup.py
4. Affichez le contenu du dossier devops_bash
5. Supprimez le fichier app_backup.py

>### Solution :
>
>```bash
>mkdir devops_bash
>
>cd devops_bash
>touch app.py requirements.txt README.md
>
>cp app.py app_backup.py
>
>ls -l
>
>rm app_backup.py
>```

# Exercice 2 : Écriture d'un script Bash simple

Écrivez un script backup.sh qui copie tous les fichiers .py du dossier courant vers un dossier backup (à créer s'il n'existe pas).

>### Solution :
>
>```bash
>#!/bin/bash
>
># Vérifier si le dossier backup existe, sinon le créer
>if [ ! -d "backup" ]; then
>  mkdir backup
>  echo "Dossier 'backup' créé."
>else
>  echo "Dossier 'backup' déjà existant."
>fi
>
># Copier les fichiers .py dans le dossier backup
>cp *.py backup/
>
>echo "Backup des fichiers .py terminé."
>```

# Exercice 3 : Archiver un répertoire

Créer un script Bash qui archive un répertoire donné et affiche la taille de l’archive.

>### Solution :
>
>```bash
>#!/bin/bash
>
># Vérifier si un répertoire est fourni en argument
>if [ -z "$1" ]; then
>  echo "J'ai besoin d'un répertoire à archiver."
>  exit 1
>fi
>
>DOSSIER=$1
>ARCHIVE=$1.tar.gz
>
># Archiver le répertoire
>tar -czf $ARCHIVE $DOSSIER
>
># Afficher la taille de l'archive
>SIZE=$(du -sh $ARCHIVE | cut -f1)
>echo "L'archive $ARCHIVE a une taille de $SIZE."
>```

# Exercice 4 : Surveillance du CPU

Écrire un script qui surveille l'utilisation du CPU et enregistre dans un fichier si l'utilisation dépasse 80%.

>### Solution :
>
>```bash
>#!/bin/bash
>
># Surveillance de l'utilisation du CPU
>THRESHOLD=10
>LOGFILE="cpu_usage.log"
>
>while true; do
>  # récupération usage CPU (et mémoire)
>  CPU=$(mpstat 1 1 | awk 'NR==4{print 100 - $NF}')
>  CPU_INT=$(echo $CPU | cut -d',' -f1)
>  Mem=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
>  
>  echo "Utilisation CPU : $CPU %"
>  echo "Utilisation Mémoire : $Mem"
>  
>  # test CPU supérieur au seuil et écriture dans le fichier .log si condition vérifiée
>  if (( CPU_INT > THRESHOLD )); then
>    echo "$(date) - Utilisation du CPU : $CPU% / Utilisation Mémoire : $Mem" >> $LOGFILE
>  fi
>
>  sleep 3
>done
>```
