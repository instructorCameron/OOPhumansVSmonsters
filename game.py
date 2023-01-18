from classes.humans import wizard, ninja, pirate, human
from classes.monsters import ghoul, zombie

michelangelo = ninja.Ninja("Michelanglo")
jack_sparrow = pirate.Pirate("Jack Sparrow")
gandalf = wizard.Wizard("Gandalf")
gollum = ghoul.Ghoul("Gollum")
lich_king = zombie.Zombie("Lich King")
# jack_sparrow.show_stats()
# michelangelo.attack(gollum)
# # jack_sparrow.show_stats()
jack_sparrow.attack(gollum)
gollum.attack(michelangelo)
gollum.attack(michelangelo)
jack_sparrow.attack(gollum, jack_sparrow.weapon['sword'])
gandalf.attack(gollum, gandalf.weapon).attack(lich_king)
jack_sparrow.attack(lich_king, jack_sparrow.weapon['dagger'])
gollum.attack(michelangelo)
lich_king.attack(jack_sparrow, lich_king.weapon)
gandalf.attack(lich_king)

jack_sparrow.show_stats()
gollum.show_stats()
michelangelo.show_stats()
gandalf.show_stats()
lich_king.show_stats()
print(michelangelo)
print(human.Human.all_humans())