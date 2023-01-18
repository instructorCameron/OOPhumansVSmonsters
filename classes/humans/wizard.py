
from classes.humans.human import Human
from classes.weapons import staff

class Wizard(Human):
  def __init__( self , name):
    super().__init__()
    self.name = name
    self.strength = 5
    self.speed = 3
    self.intellect = 50
    self.weapon = staff.Staff(self.intellect)
