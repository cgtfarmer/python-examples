class Player:
  def __init__(self, name, level, hp, strength):
    self.name = name
    self.level = level
    self.hp = hp
    self.strength = strength

  def attack(self, enemy):
    print(f'\n{self.name} is attacking {enemy.name}...')

    print(f'Did {self.strength} damage!')

    enemy.receiveDamage(self.strength)

  def receiveDamage(self, damage):
    self.hp = (self.hp - damage)

    if self.hp <= 0:
      self.die()

  def die(self):
    print(f'{self.name} fainted!')

  def getStatus(self):
    return f'[{self.name}] Lvl: {self.level}, HP: {self.hp}, Strength: {self.strength}'

def main():
  player1 = Player("Acryce", 99, 100, 90)

  player2 = Player("Arsidee", 15, 100, 5)

  player2.attack(player1)

  printBattleStatus(player1, player2)

  player1.attack(player2)

  printBattleStatus(player1, player2)

  player2.attack(player1)

  printBattleStatus(player1, player2)

  player1.attack(player2)

  printBattleStatus(player1, player2)

def printBattleStatus(player, enemy):
  print(f'\n{player.getStatus()}\n{enemy.getStatus()}')

if __name__ == '__main__':
  main()
