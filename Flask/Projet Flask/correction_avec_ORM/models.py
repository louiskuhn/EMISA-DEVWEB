from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.Enum('male', 'female', name='sex_enum'), nullable=False)
    pseudo = db.Column(db.String(255), unique=True, nullable=False)