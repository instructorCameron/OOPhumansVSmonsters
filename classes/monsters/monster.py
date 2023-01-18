from classes.player import Player
class Monster(Player):
  total_monsters = 0
  def __init__(self):
    super().__init__()
    Monster.total_monsters += 1
    Player.total_players += 1

  def attack ( self , victim, weapon = False ):
    return super().attack( victim, weapon)

  def show_stats( self ):
    super().show_stats()
