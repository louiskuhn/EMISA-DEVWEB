from flask import Flask, url_for, render_template, request, flash, redirect
import os
from datetime import datetime
import base64

from database import mariadb_connection, get_or_create_table, add_new_user, get_all_users

# Initialisation de l'appli
app = Flask(__name__)

# Configuration de l'application
app.config["SECRET_KEY"] = "a_secret_key"
app.config["UPLOAD_FOLDER"] = "static/images"

# On s'assure que le dossier d'upload existe
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Page d'accueil
@app.route("/")
def home():
    return render_template("home.html")

###################################
#######   QUESTIONS 1 à 6   #######
###################################
#Page de formulaire, envoi des données et affichage du message de bienvenu
@app.route("/test-formulaire", methods=["GET", "POST"])
def formulaire():
    if request.method == "POST":
        prenom = request.form["prenom"]
        nom = request.form["nom"]
        sex = request.form["sex"]
        user = request.form["user"]

        #Connection de la base de données et de la table users
        db = mariadb_connection()
        curseur = get_or_create_table(db)
        new_user_ok = add_new_user(db, curseur, prenom, nom, sex, user)

        if new_user_ok:
            flash("Compte crée avec succès !", "success")
            return render_template("greetings.html", prenom=prenom, nom=nom, sex=sex, user=user) #on renvoie le html greetings avec la petite phrase de bienvenue
        else:
            flash("Ce pseudo est déjà pris...", "warning")
            return redirect(url_for('formulaire'))

    return render_template("formpage.html")

#Page d'affichage des utilisateurs inscrits dans la bdd
@app.route("/utilisateurs-inscrits")
def see_users():
    liste = get_all_users()

    if liste:
        return render_template("userspage.html", liste_users=liste)
    else:
        flash("Problème de connexion à la base de données...créer des utilisateurs !", "error")
        return redirect(url_for('formulaire'))        



##################################
#######     QUESTION 7     #######
##################################
@app.route("/dessin")
def dessin():
    return render_template("dessin.html")
    
#récupération de l'image et sauvegarde
@app.route('/dessin', methods=['POST'])
def save_image():
    img_data = request.form.get('data')

    # Supprimer le préfixe base64
    img_data = img_data.replace("data:image/png;base64,", "")
    img_bytes = base64.b64decode(img_data)

    # Nom de fichier unique avec timestamp
    file_name = f"canvas_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

    # Sauvegarde de l'image
    with open(file_path, "wb") as file:
        file.write(img_bytes)
    
    return render_template("dessin.html", last_img=url_for('static', filename=f'images/{file_name}'))


#on lance le serveur pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True)
