
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
  
  
  def show_stats( self ):
    print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nIntellect: {self.intellect}\nHealth: {self.health}\nIsLiving: {self.isLiving}\n")
  
  
  # def can_attack(attacker):
  #   return super().can_attack(attacker)

  # def attack(self, victim, weapon=False):
  #   return super().attack(victim, weapon)

  # def all_humans():
  #   Human.all_humans()
    
  # @staticmethod
  # def can_attack(attacker):
  #   return super().can_attack(attacker)