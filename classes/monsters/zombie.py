from classes.monsters.monster import Monster
from classes.weapons import staff

class Zombie(Monster):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.strength = 10
    self.speed = 15
    self.intellect = 50
    self.weapon = staff.Staff(self.intellect)
