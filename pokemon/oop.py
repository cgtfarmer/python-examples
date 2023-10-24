class Ability:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

class Pokemon:
  def __init__(self, name, hp, ability1, ability2, ability3, ability4):
    self.name = name
    self.hp = hp
    self.ability1 = ability1
    self.ability2 = ability2
    self.ability3 = ability3
    self.ability4 = ability4

  def attack(self, pokemon, abilityNumber):
    ability = self._getAbilityByNumber(abilityNumber)

    print(f'\n{self.name} is attacking {pokemon.name} with {ability.name}...')

    print(f'Did {ability.damage} damage!')

    pokemon.hp = (pokemon.hp - ability.damage)

    if pokemon.hp <= 0:
      print(f'{pokemon.name} fainted!')

  def getStatus(self):
    return f'{self.name}: {self.hp}'

  def _getAbilityByNumber(self, number):
    if number == 1:
      return self.ability1
    elif number == 2:
      return self.ability2
    elif number == 3:
      return self.ability3
    elif number == 4:
      return self.ability4
    else:
      return None

abilities = [
  Ability('Tackle', 10),
  Ability('Thundershock', 25)
]

pokemon = [
  Pokemon('Caterpie', 100, abilities[0], None, None, None),
  Pokemon('Pikachu', 100, abilities[0], abilities[1], None, None)
]

def main():
  pokemon[1].attack(pokemon[0], 1)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[0].attack(pokemon[1], 1)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[1].attack(pokemon[0], 2)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[0].attack(pokemon[1], 1)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[1].attack(pokemon[0], 2)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[1].attack(pokemon[0], 2)
  printBattleStatus(pokemon[1], pokemon[0])

  pokemon[1].attack(pokemon[0], 2)
  printBattleStatus(pokemon[1], pokemon[0])

def printBattleStatus(pokemon1, pokemon2):
  print(f'\n{pokemon1.getStatus()}\n{pokemon2.getStatus()}')

if __name__ == '__main__':
  main()
