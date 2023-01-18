from classes.player import Player
class Human(Player):
  total_humans = 0
  def __init__(self):
    super().__init__()
    Human.total_humans += 1
    Player.total_players += 1

  def attack ( self , victim, weapon = False ):
    return super().attack( victim, weapon)

  def show_stats( self ):
    super().show_stats()

