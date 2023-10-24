abilities = [
  { 'name': 'Tackle', 'damage': 10 },
  { 'name': 'Thundershock', 'damage': 25 }
]

pokemon = [
  { 'name': 'Caterpie', 'hp': 100, 'ability1': abilities[0], 'ability2': None },
  { 'name': 'Pikachu', 'hp': 100, 'ability1': abilities[1], 'ability2': abilities[0] }
]

def main():
  attack(pokemon[1], pokemon[0], 'ability2')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[0], pokemon[1], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[1], pokemon[0], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[0], pokemon[1], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[1], pokemon[0], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[1], pokemon[0], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

  attack(pokemon[1], pokemon[0], 'ability1')
  printBattleStatus(pokemon[1], pokemon[0])

def attack(attacker, recipient, abilityChoice):
  ability = attacker[abilityChoice]
  damage = ability["damage"]

  print(f'\n{attacker["name"]} is attacking {recipient["name"]} with {ability}...')

  print(f'Did {damage} damage!')

  recipient['hp'] = (recipient['hp'] - damage)

  if recipient['hp'] <= 0:
    print(f'{recipient["name"]} fainted!')

def printBattleStatus(pokemon1, pokemon2):
  print(f'\n{createBattleStatus(pokemon1)}\n{createBattleStatus(pokemon2)}')

def createBattleStatus(pokemon):
  return f'{pokemon["name"]}: {pokemon["hp"]}'

if __name__ == '__main__':
  main()
