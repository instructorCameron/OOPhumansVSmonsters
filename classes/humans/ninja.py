from classes.humans.human import Human
from classes.weapons import dagger

class Ninja(Human):
    def __init__( self , name):
        super().__init__()
        self.name = name
        self.strength = 10
        self.speed = 6
        self.weapon = dagger.Dagger(self.strength)

