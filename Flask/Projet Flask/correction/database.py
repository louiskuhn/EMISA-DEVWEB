import mariadb
import os

# Paramètres de connexion MariaDB
DB_USR = os.getenv("mariadb_usr")
DB_PWD = os.getenv("mariadb_pwd")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "emisa_flask_db")

def mariadb_connection():
    # Connection à MariaDB
    db = mariadb.connect(
        host=DB_HOST,
        user=DB_USR, 
        password=DB_PWD,
        unix_socket="/run/mysqld/mysqld.sock",
    )
    
    return db

def get_or_create_table(db):
    curseur = db.cursor()
    curseur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    curseur.execute(f"USE {DB_NAME}")
    curseur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            prenom VARCHAR(255),
            nom VARCHAR(255),
            sex ENUM('male', 'female'),
            pseudo VARCHAR(255),
            UNIQUE(pseudo)
        )
        """
    )

    return curseur


def add_new_user(db, curseur, prenom, nom, sex, user):

    try : #on essaye d'ajouter la ligne dans la base
        insert_query = "INSERT INTO users (prenom, nom, sex, pseudo) VALUES (%s, %s, %s, %s)"
        values = (prenom, nom, sex, user)
        curseur.execute(insert_query, values)
        db.commit()
        curseur.close()
        db.close() 
        return True

    except mariadb.Error: #comme on a mis le pseudo en unique, s'il y a 2 fois le même, il y aura une erreur lors de l'insertion
        db.rollback()
        curseur.close()
        db.close()
        return False
    
def get_all_users(database=DB_NAME, table='users'):
    db = mariadb_connection()
    curseur = db.cursor()

    try: #on essaye de se connecter à la bdd
        curseur.execute(f"USE {DB_NAME}")
        curseur.execute(f"SELECT * FROM {table}") #si ça marche, on récupère les users
        liste_users = curseur.fetchall()
        curseur.close()
        db.close()
        return liste_users
    
    except mariadb.Error:#sinon on retourne un message d'erreur et on renvoie au formulaire
        db.rollback()
        curseur.close()
        db.close()
        return None