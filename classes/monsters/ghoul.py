from classes.monsters.monster import Monster

class Ghoul(Monster):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.strength = 5
    self.speed = 7
