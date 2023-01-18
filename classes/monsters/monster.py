class Monster:
  def __init__(self):
    self.health = 100
    self.isLiving = True

  def attack ( self , victim, weapon = False ):
    if self.isLiving:
      if victim.isLiving:
        if weapon:
          victim.health -= weapon.damage
        else:
          victim.health -= self.strength
        if victim.health <= 0:
          victim.isLiving = False
          print(f"You are the victor over {victim.name}.\n")
      else:
        print(f"Dont kick a dead {victim.name}.\n")
    else:
      print(f"You cant attack {victim.name}... your dead.\n")
    return self

  def show_stats( self ):
    print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nIsLiving: {self.isLiving}\n")