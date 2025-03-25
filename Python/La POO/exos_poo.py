### Exercice 1
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")

iban = Personne("Paul", 18)
iban.se_presenter()

print("---------------------------------------")
### Exercice 2
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def ajouter_stock(self, quantite):
        self.quantite += quantite

    def retirer_stock(self, quantite):
        if self.quantite >= quantite:
            self.quantite -= quantite
        else:
            print("Stock insuffisant")
    
ordi = Produit("ordinateur", 800, 5)
print(ordi.quantite)
ordi.ajouter_stock(3)
print(ordi.quantite)
ordi.retirer_stock(10)
ordi.retirer_stock(4)
print(ordi.quantite)
ordi.quantite = 0
print(ordi.quantite)

print("---------------------------------------")
### Exercice 3
class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre {self.titre} a bien été emprunté")            
        else:
            print(f"Le livre {self.titre} n'est pas disponible")

    def retourner(self):
        self.disponible = True
        print(f"Le livre {self.titre} a été retourné")

livre = Livre("Harry Potter 1", "Rowling")
livre2 = Livre("Harry Potter 2", "Rowling", False)
livre.emprunter()
livre2.emprunter()
livre2.retourner()
livre2.emprunter()


print("---------------------------------------")
### Exercice 4
class Chambre:
    def __init__(self, numero, libre=True):
        self.numero = numero
        self.libre = libre

    def reserver(self):
        if self.libre:
            self.libre = False
            print(f"La chambre {self.numero} a bien été réservée")            
        else:
            print(f"La chambre {self.numero} n'est pas libre")

    def liberer(self):
        self.libre = True
        print(f"La chambre {self.numero} a été libérée")

class Hotel:
    def __init__(self, nom, nb_chambre):
        self.nom = nom
        self.chambres = [Chambre(i) for i in range(1, nb_chambre+1)]

    def afficher_etats(self):
        for chambre in self.chambres:
            etat = "libre" if chambre.libre else "occupée"
            print(f"Chambre {chambre.numero} : {etat}")

hotel = Hotel("Georges", 5)
hotel.afficher_etats()
hotel.chambres[0].reserver()
hotel.afficher_etats()