from classes.humans.human import Human
from classes.weapons import dagger, sword

class Pirate(Human):
    def __init__( self , name ):
        super().__init__()
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 130
        self.weapon = {
            'sword': sword.Sword(self.strength),
            'dagger': dagger.Dagger(self.strength)
            }

