# Exercice 1 : Installation et configuration de Jenkins avec Docker

On va installer et configurer Jenkins dans un conteneur Docker en incluant l'accès au Docker du système hôte pour les builds.


1. Télécharger l'image Jenkins
   ```bash
   docker pull jenkins/jenkins:lts
   ```
   Cette commande télécharge l'image Docker officielle de Jenkins.

2. Lancer le conteneur Jenkins avec un accès à Docker

    Pour ça, on va lancer un conteneur Jenkins en lui permettant d'accéder au Docker de l'hôte en :
    - montant le socket Docker (`/var/run/docker.sock`) pour permettre la communication avec le moteur Docker.
    - montant le binaire Docker pour que le client Docker soit directement accessible dans le conteneur.
    - configurant les permissions nécessaires en ajoutant le groupe Docker de l'hôte dans le conteneur.

    ```bash
    docker run -d -p 8080:8080 -p 50000:50000 \
    -v jenkins_home:/var/jenkins_home \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $(which docker):$(which docker) \
    --group-add 999 \
    --name jenkins jenkins/jenkins:lts
    ```

    Explications

    - `docker run -d` : lance le conteneur en mode détaché (en arrière-plan)

    - `-p 8080:8080` : expose le port 8080 du conteneur (port par défaut de Jenkins) sur le port 8080 de l'hôte
    
    - `-p 50000:50000` : expose le port 50000 pour permettre la communication entre Jenkins et les agents distants, si nécessaire

    - `-v jenkins_home:/var/jenkins_home` : monte un volume Docker nommé `jenkins_home` dans le répertoire `/var/jenkins_home` du conteneur pour la persistance des données Jenkins (jobs, configurations, plugins), même si le conteneur est redémarré ou supprimé

    - `-v /var/run/docker.sock:/var/run/docker.sock` : monte le socket Docker de l'hôte dans le conteneur, ce qui permet au conteneur Jenkins de communiquer avec le moteur Docker de l'hôte pour exécuter des commandes Docker

    - `-v $(which docker):$(which docker)` : monte le binaire Docker (généralement `/usr/bin/docker`) dans le conteneur. Nécessaire car, par défaut, le conteneur Jenkins n'a pas le client Docker installé. En montant directement le client Docker de l'hôte dans le conteneur, on évite d'avoir à installer Docker dans le conteneur lui-même

    - `--group-add 999` : ajoute le groupe avec l'ID `999` (généralement le groupe Docker de l'hôte) au conteneur Jenkins et donc donne aux processus de Jenkins les permissions nécessaires pour accéder à Docker via le socket monté

    - `--name jenkins` : nom du conteneur `jenkins`

    - `jenkins/jenkins:lts` : image Docker officielle Jenkins LTS

3. Accéder à l'interface Jenkins :
   - Ouvrez un navigateur et allez à `http://localhost:8080`.
   - Obtenez le mot de passe initial de connexion :
     ```bash
     docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
     ```
   - Utilisez ce mot de passe pour vous connecter et complétez la configuration initiale.

4. Installation des Plugins :
   - Allez dans *Manage Jenkins > Manage Plugins > Available*.
   - Recherchez et installez les plugins **Git**, **Docker**, et **Pipeline**.
   - Ces plugins sont nécessaires pour le CI/CD avec des conteneurs et des référentiels Git.


# Exercice 2 : Création d'un Job Freestyle avec Docker

On va vérifier que Jenkins peut exécuter des commandes Docker depuis un _job freestyle_, en utilisant une commande simple.

1. Créer un Job Freestyle dans Jenkins :
   - Allez dans l'interface Jenkins, cliquez sur *New Item*.
   - Nommez le job `DockerHello` et sélectionnez *Freestyle project*.
   - Cliquez sur *OK* pour créer le job.

2. Configurer le Job pour Exécuter Docker :
   - Dans la section *Build*, sélectionnez *Execute shell* et entrez la commande suivante :
     ```bash
     docker run hello-world
     ```
   - Cette commande démarre un conteneur qui affiche un message de bienvenue pour vérifier que Docker fonctionne.

3. Exécuter le Job et Vérifier la Sortie :
   - Cliquez sur *Save* pour enregistrer le job, puis lancez-le en cliquant sur *Build Now*.
   - Allez dans *Console Output* pour vérifier la sortie : si c'est ok, vous verrez le message Docker de `hello-world`.


# Exercice 3 : Création d'un Pipeline CI/CD pour l'Application Flask

On va, progressivement rassurez-vous, configurer un pipeline Jenkins pour construire, tester et déployer l'application Flask dans un conteneur Docker.

1. Créer le Dépôt Git pour l'Application Flask :
   - Créez un dépôt Git pour l'application Flask.
   - Poussez les fichiers suivants dans le dépôt :
     - `app.py` : fichier principal de l'application Flask
        ```python
        from flask import Flask

        app = Flask(__name__)

        @app.route('/')
        def home():
            return "Un peu de CI/CD avec Git, Jenkins et Docker!"

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000)
        ```
     - `requirements.txt` : pour les dépendances
        ```
        Flask
        ```    
     - `Dockerfile` : pour la création de l'image Docker
        ```docker
        # Utiliser l'image Python comme base
        FROM python:3.8-slim

        # Copier les fichiers de l'application dans le conteneur
        COPY . /app
        WORKDIR /app

        # Installer les dépendances
        RUN pip install -r requirements.txt

        # Exposer le port de l'application
        EXPOSE 5000

        # Commande pour lancer l'application
        CMD ["python", "app.py"]
        ```
     - `Jenkinsfile` : pour définir le pipeline
        ```groovy
        pipeline {
            agent any
            environment {
                IMAGE_NAME = "flask_app"
            }
            stages {
                stage('Checkout') {
                    steps {
                        git branch: 'main', url: 'https://github.com/louiskuhn/flask_app'
                    }
                }
                stage('Build Docker Image') {
                    steps {
                        echo 'Building the Docker image...'
                        sh 'docker build -t $IMAGE_NAME .'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying application...'
                        sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
                    }
                }
            }
            post {
                always {
                    echo 'Pipeline terminé.'
                }
            }
        }
        ```

2. Configurer un Job Pipeline dans Jenkins :
   - Dans Jenkins, cliquez sur *New Item*, entrez un nom `FlaskAppPipeline`, et sélectionnez *Pipeline*.
   - Dans la configuration du job, allez à la section *Pipeline* et sélectionnez *Pipeline script from SCM*.
   - Dans le champ *SCM*, choisissez Git et ajoutez l'URL de votre dépôt.
   - Assurez-vous que le `Jenkinsfile` est bien dans la racine du dépôt pour que Jenkins puisse le lire.

3. Tester le Pipeline :
   - Exécutez le pipeline en cliquant sur *Build Now*.
   - Vérifiez chaque étape dans *Stage View* pour s'assurer qu'elles sont passées sans erreur.
   - Testez l'application en accédant à `http://localhost:5000`.

4. Ajouter une étape de Test avec un simple test unitaire PyTest :
    - Créez et ajoutez un fichier de test `test_app.py` dans le même répertoire que `app.py` :
        ```python
        import pytest
        from app import app

        @pytest.fixture
        def client():
            # Configure l'application pour le test
            app.config['TESTING'] = True
            with app.test_client() as client:
                yield client

        def test_home(client):
            # Teste que la route '/' retourne le texte attendu
            response = client.get('/')
            assert response.status_code == 200
            assert response.data == b"Un peu de CI/CD avec Git, Jenkins et Docker!"
        ```
    - Mettez à jour le `requirements.txt` en ajoutant une ligne `pytest`
    - Mettez à jour le `Jenkinsfile` pour ajouter l'étape de test suivante:
        ```groovy
        stage('Test') {
            steps {
                echo 'Running tests with pytest...'
                sh 'docker run --rm $IMAGE_NAME pytest'
            }
        }
        ```

# Exercice 4 : Déclenchement Automatique du Build à chaque Push sur le Dépôt

Cet exercice vous permet de configurer un déclenchement automatique du pipeline Jenkins à chaque modification (*push*) sur le dépôt Git.

1. Configurer le Webhook dans le Dépôt Git :
   - Allez dans votre dépôt GitHub, puis dans *Settings* > *Webhooks* > *Add webhook*.
   - Dans le champ Payload URL, entrez l'URL de votre Jenkins suivie de `/github-webhook/`.  
        >*Remarque : dans notre cas, on utilise un conteneur docker avec Jenkins sur le localhost et les webhooks de Git nécessitent une adresse public, on va contourner le problème en utilisant ngrok pour faire un tunnel entre notre port 8080 et les internets...* 
   - Sélectionnez le type d'événement : choisissez *Just the push event* pour déclencher Jenkins uniquement lors des `push`.
   - Cliquez sur *Add webhook* pour enregistrer.

2. Configurer Jenkins pour le Déclenchement Automatique : dans la configuration de votre job *Pipeline*, cochez la case **GitHub hook trigger for GITScm polling** dans la section *Build Triggers* pour déclencher le pipeline automatiquement à chaque *push* sur GitHub

3. Tester le Déclenchement Automatique :
   - Faites une modification dans votre code local, puis un `git push` vers le dépôt
   - Allez dans l'interface Jenkins et vérifiez que le pipeline a démarré automatiquement en réponse au *push*
   - Vous pouvez également vérifier les logs du *Webhook* dans GitHub pour voir si le webhook a été appelé avec succès