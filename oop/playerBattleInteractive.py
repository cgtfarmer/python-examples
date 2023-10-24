import random

class Player:
  def __init__(self, name, level, hp, strength, magic):
    self.name = name
    self.level = level
    self.hp = hp
    self.strength = strength
    self.magic = magic

  def attack(self, enemy):
    print(f'\n{self.name} is attacking {enemy.name}...')

    print(f'Did {self.strength} damage!')

    enemy.receiveDamage(self.strength)

  def receiveDamage(self, damage):
    self.hp = (self.hp - damage)

    if self.isDead():
      self.die()

  def heal(self):
    self.hp = (self.hp + self.magic)

    print(f'Healed {self.magic} hp!')

  def die(self):
    print(f'{self.name} fainted!')

  def isDead(self):
    return (self.hp <= 0)

  def getStatus(self):
    return f'[{self.name}] Lvl: {self.level}, HP: {self.hp}, Strength: {self.strength}, Magic: {self.magic}'

validMenuChoices = ["1", "2", "3", "4"]

def main():
  enemy = Player("Badb0i", 15, 80, 5, 5)

  playerName = getPlayerNameInput()
  player = Player(playerName, 50, 100, 25, 10)

  while True:
    handlePlayerTurn(player, enemy)

    handleEnemyTurn(player, enemy)

    if player.isDead() or enemy.isDead():
      break

  print("GAME OVER")

  printResults(player, enemy)

def handlePlayerTurn(player, enemy):
  choice = getMenuInput(player, enemy)

  if choice == "1":
    player.attack(enemy)
  elif choice == "2":
    player.heal()
  elif choice == "3":
    print("Doing nothing...")
  else:
    raise Exception("This should be impossible")

def handleEnemyTurn(player, enemy):
  choice = random.randint(0, 1)

  if choice == 0:
    enemy.attack(player)
  elif choice == 1:
    enemy.heal()
  else:
    raise Exception("This should be impossible")

def getPlayerNameInput():
  return input("Input player name: ").strip()

def getMenuInput(player, enemy):
  while True:
    printMenu()
    choice = input("Choice: ").strip()

    if choice not in validMenuChoices:
      continue

    if choice == "4":
      printBattleStatus(player, enemy)
      continue

    return choice

def printMenu():
  print("Menu: 1=attack, 2=heal, 3=nothing, 4=status")

def printBattleStatus(player, enemy):
  print(f'\n{player.getStatus()}\n{enemy.getStatus()}')

def printResults(player, enemy):
  print("Final Results:")
  printBattleStatus(player, enemy)

  print()

  if player.isDead():
    print("You lost!")
  elif enemy.isDead():
    print("You win!")
  else:
    raise Exception("This should be impossible")

if __name__ == '__main__':
  main()
