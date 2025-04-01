from flask import Flask, render_template, request, flash, redirect, url_for
import os
import base64
from datetime import datetime

from models import db, User

# Initialisation de l'appli
app = Flask(__name__)

# Paramètres de connexion MariaDB
DB_USR = os.getenv("mariadb_usr")
DB_PWD = os.getenv("mariadb_pwd")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "emisa_flask_db")

# Configuration de l'application
app.config["SECRET_KEY"] = "a_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USR}:{DB_PWD}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "static/images"

# On s'assure que le dossier d'upload existe
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Initialisation de la bdd
db.init_app(app)

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
        pseudo = request.form["user"]

        try:
            new_user = User(prenom=prenom, nom=nom, sex=sex, pseudo=pseudo)
            db.session.add(new_user)
            db.session.commit()
            flash("Compte créé avec succès !", "success")
            return render_template("greetings.html", prenom=prenom, nom=nom, sex=sex, user=pseudo)
        
        except:
            db.session.rollback()
            flash("Ce pseudo est déjà pris...", "warning")
            return redirect(url_for('formulaire'))

    return render_template("formpage.html")

@app.route("/utilisateurs-inscrits")
def see_users():
    users = User.query.all()

    if users:
        return render_template("userspage.html", liste_users=users)
    else:
        flash("Aucun utilisateur trouvé.", "warning")
        return redirect(url_for('formulaire'))


##################################
#######     QUESTION 7     #######
##################################
@app.route("/dessin")
def dessin():
    return render_template("dessin.html")

@app.route('/dessin', methods=['POST'])
def save_image():
    img_data = request.form.get('data')
    img_data = img_data.replace("data:image/png;base64,", "")
    img_bytes = base64.b64decode(img_data)

    file_name = f"canvas_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

    with open(file_path, "wb") as file:
        file.write(img_bytes)
    
    return render_template("dessin.html", last_img=url_for('static', filename=f'images/{file_name}'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Pour s'assurer que les tables sont créées
    app.run(debug=True)