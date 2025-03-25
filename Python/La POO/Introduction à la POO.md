# Introduction à la Programmation Orientée Objet (POO) en Python

## 1. Introduction
La Programmation Orientée Objet (POO) est un paradigme de programmation qui repose sur la modélisation du monde réel sous forme d'objets. En Python, la POO permet d'écrire du code modulaire, réutilisable et facile à maintenir.

#### Quelques ressources
- https://datascientest.com/programmation-orientee-objet-guide-ultime
- https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants

## 2. Concepts Fondamentaux
### 2.1 Classes et Objets
Une classe est un modèle permettant de créer des objets. Un objet est une instance de classe.

```python
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_infos(self):
        print(f"{self.marque} {self.modele}, Année: {self.annee}")

# Création d'un objet
ma_voiture = Voiture("Toyota", "Corolla", 2020)
ma_voiture.afficher_infos()
```

### 2.2 Encapsulation
L'encapsulation consiste à protéger les données d'un objet en les rendant accessibles uniquement via des méthodes.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde de {self.titulaire}: {self.__solde} EUR")

# Utilisation
compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.afficher_solde()
```

### 2.3 Getters et Setters
Les getters et setters permettent de contrôler l'accès aux attributs d'une classe.

```python
class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    def get_nom(self):
        return self.__nom

    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def get_age(self):
        return self.__age

    def set_age(self, nouvel_age):
        if nouvel_age > 0:
            self.__age = nouvel_age
        else:
            print("L'âge doit être positif.")

personne = Personne("Alice", 25)
print(personne.get_nom())
personne.set_age(30)
print(personne.get_age())
```

### 2.4 Héritage
L'héritage permet de créer une nouvelle classe basée sur une classe existante.

```python
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher_infos(self):
        print(f"Véhicule: {self.marque} {self.modele}")

class Moto(Vehicule):
    def __init__(self, marque, modele, cylindree):
        super().__init__(marque, modele)
        self.cylindree = cylindree

    def afficher_infos(self):
        print(f"Moto: {self.marque} {self.modele}, Cylindrée: {self.cylindree}cc")

moto = Moto("Yamaha", "R1", 1000)
moto.afficher_infos()
```

### 2.5 Polymorphisme
Le polymorphisme permet d'utiliser une même interface pour différents types d'objets.

```python
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Miaou!"

animaux = [Chien(), Chat()]
for animal in animaux:
    print(animal.parler())
```

## 3. Exercices

### Exercice 1: Création d'une classe `Personne`

Créez une classe `Personne` avec un constructeur prenant en paramètre `nom` et `age`. Ajoutez une méthode `se_presenter()` affichant "Je m'appelle X et j'ai Y ans."

### Exercice 2: Gestion d'un stock de produits

Créez une classe `Produit` avec `nom`, `prix` et `quantite`. Implémentez les méthodes `ajouter_stock()` et `retirer_stock()`.

### Exercice 3: Système de gestion de bibliothèque

Créez une classe `Livre` avec `titre`, `auteur` et un attribut `disponible`. Ajoutez des méthodes `emprunter()` et `retourner()` pour gérer l'état du livre.

### Exercice 4: Système de réservation d'hôtel

Créez une classe `Chambre` avec un numéro et un état (`occupée` ou `libre`). Implémentez des méthodes `reserver()` et `liberer()`. Créez une classe `Hotel` contenant plusieurs chambres et permettant d'afficher leur état.


### Exercices complémentaires

Toute une série de petits exercices corrigés disponibles au lien suivant :
https://www.tresfacile.net/tp-poo-et-les-classes-en-python3-exercices-avec-solutions/
