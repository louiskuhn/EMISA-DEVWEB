# Exercices POO avec Python

La classe `Robot` modélise l'état et le comportement de robots virtuels. Chaque robot correspond à un objet qui est une instance de cette classe.

Chaque robot :
* a un nom (attribut nom : chaîne de caractères)
* a une position : donnée par les attributs entiers x et y, sachant que x augmente en allant vers l'Est et y augmente en allant vers le Nord,
* a une direction : donnée par l'attribut direction qui prend une des valeurs "Nord", "Est", "Sud" ou "Ouest"
* peut avancer d'un pas en avant : avec la méthode avance()
* peut tourner à droite de 90° pour changer de direction (si sa direction était "Nord" elle devient "Est", si c'était "Est" elle devient "Sud", etc.) : avec la méthode sans paramètre droite(). Les robots ne peuvent pas tourner à gauche.
* peut aﬃcher son état en détail

Le nom, la position et la direction d'un robot lui sont donnés au moment de sa création. Le nom est obligatoire mais on peut ne pas spécifier la position et la direction, qui sont définis par défaut à (0,0) et "Est".

1. Écrire les instructions Python qui permettent de définir la classe `Robot`, en respectant le principe de l'encapsulation des données.

2. On veut améliorer ces robots en en créant une nouvelle génération de robots les `RobotNG` qui ne remplacent pas les anciens robots mais peuvent cohabiter avec eux. Écrire cette nouvelle classe en spécialisant celle de la première question, sans modifier celle-ci.  
Les `RobotNG` savent faire la même chose mais aussi :
>- avancer de plusieurs pas en une seule fois grâce à une méthode avance() qui prend en paramètre le nombre de pas
>- tourner à gauche de 90° grâce à la méthode gauche()
>- faire demi-tour grâce à la méthode demiTour()

3. Enfin, modifier la classe `RobotNG` pour pouvoir activer un mode « Turbo » et le désactiver. Dans ce mode, chaque pas est multiplié par 3. L'appel à la méthode aﬃcher() devra indiquer à la fin si le robot est en mode Turbo ou pas.

