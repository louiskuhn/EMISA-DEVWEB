class Robot():
    directions = ['Est', 'Sud', 'Ouest', 'Nord']
    deplacements = {
        'Est': (1,0),
        'Sud': (0,-1),
        'Ouest': (-1,0),
        'Nord': (0,1),
    }

    def __init__(self, nom, x=0, y=0, direction="Est"):
        self.nom = nom
        self.x = x
        self.y = y
        self.direction = direction
        self.histo = ""

    def avance(self):
        self.histo += f"\n{(self.x, self.y)}, {self.direction}"
        dx, dy = Robot.deplacements[self.direction]
        self.x = self.x + dx
        self.y = self.y + dy
        return self

    def droite(self):
        self.histo += f"\n{(self.x, self.y)}, {self.direction}"
        idx_direction_actuelle = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(idx_direction_actuelle + 1) % 4]
        return self
    
    def etat(self, with_history=False):
        print(f"{self.nom} est en {(self.x, self.y)} orienté vers {self.direction}")
        if with_history:
            print(f"après être passé par :{self.histo} ")

r1 = Robot("Wall-E")
r1.avance().droite().avance().droite()
# r1.etat(True)

class RobotNG(Robot):
    def __init__(self, nom, x=0, y=0, direction="Est", turbo=False):
        super().__init__(nom, x, y, direction)
        self.turbo = turbo

    def avance(self, nb_pas=1):
        self.histo += f"\n{(self.x, self.y)}, {self.direction}"

        dx = nb_pas * Robot.deplacements[self.direction][0]
        dy = nb_pas * Robot.deplacements[self.direction][1]

        if self.turbo:
            dx *= 3
            dy *= 3

        self.x = self.x + dx
        self.y = self.y + dy

        return self

    def droite(self, nb_quarts=1):
        self.histo += f"\n{(self.x, self.y)}, {self.direction}"
        idx_direction_actuelle = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(idx_direction_actuelle + nb_quarts) % 4]
        return self
    
    def gauche(self, nb_quarts=1):
        self.histo += f"\n{(self.x, self.y)}, {self.direction}"
        idx_direction_actuelle = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(idx_direction_actuelle - nb_quarts) % 4]
        return self
    
    def turbo_onoff(self):
        if self.turbo:
            self.turbo = False
            print("Turbo désactivé")
        else:
            self.turbo = True
            print("Turbo activé")
        
        return self
    
    def etat(self, with_history=False):
        print(f"{self.nom} est en {(self.x, self.y)} orienté vers {self.direction}")
        print(f"Le turbo est {'activé' if self.turbo else 'désactivé'}")
        if with_history:
            print(f"après être passé par :{self.histo} ")
    
r1 = RobotNG("Better Wall-E")
r1.avance(5).droite(2).turbo_onoff().avance().gauche(3).turbo_onoff()
r1.etat(True)