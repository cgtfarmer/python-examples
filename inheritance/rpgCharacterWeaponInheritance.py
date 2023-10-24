import random

class Weapon:
  def __init__(self, name, strength, magic, critChance):
    self.name = name
    self.strength = strength
    self.magic = magic
    self.critChance = critChance

  def describe(self):
    print(self.toString())

  def toString(self):
    print(f'{self.name}) strength={self.hp}, magic={self.magic}, critChance={self.critChance}')

class Character:
  def __init__(self, name, hp, strength, magic, defense):
    self.name = name
    self.hp = hp
    self.strength = strength
    self.magic = magic
    self.defense = defense
    self.weapon = None

  def setWeapon(self, weapon):
    self.weapon = weapon

  def physicalAttack(self, target):
    dmg = self._computePhysicalAttackDmg()
    print(f'{self.name} attacks {target.name} for {dmg} damage')
    target.takeDamage(dmg)

  def magicalAttack(self, target):
    dmg = self._computeMagicalAttackDmg()
    print(f'\n{self.name} attacks {target.name} for {dmg} damage')
    target.takeDamage(dmg)

  def takeDamage(self, damage):
    self.hp = (self.hp - damage)

    print(f'{self.name} took {damage} damage. Health is now {self.hp}')

    if self.hp <= 0:
      self.die()

  def die(self):
    print(f'{self.name} died')

  def describe(self):
    print(self.toString())

  def toString(self):
    print(f'{self.name}) hp={self.hp}, strength={self.strength}, magic={self.magic}, defense={self.defense}, weapon={self.weapon.toString()}')

  def _computePhysicalAttackDmg(self):
    dmg = (self.strength + self.weapon.strength)

    if self._isCriticalHit():
      return (dmg * 2)

    return dmg

  def _computeMagicalAttackDmg(self):
    dmg = (self.magic + self.weapon.magic)

    if self._isCriticalHit():
      return (dmg * 2)

    return dmg

  def _isCriticalHit(self):
    critThreshold = (self.weapon.critChance * 10)

    roll = random.randint(0, 100)

    if roll < critThreshold:
      print("-- Attack is a critical hit!")
      return True

    return False

class Player(Character):
  def __init__(self, name, hp, strength, magic, defense):
    super().__init__(name, hp, strength, magic, defense)

class Goblin(Character):
  def __init__(self):
    super().__init__("Goblin", 25, 8, 3, 5)

    self.weapon = Weapon("Club", 10, 1, 0.1)

class BlackKnight(Character):
  def __init__(self):
    super().__init__("Black Knight", 50, 30, 10, 25)

    self.weapon = Weapon("Steel Longsword", 32, 5, 0.18)

class Robot(Character):
  def __init__(self):
    super().__init__("Robot", 80, 35, 45, 40)

    self.weapon = Weapon("Laser", 32, 50, 0.33)

def main():
  print("\n-- ARSIDEE BATTLE --\n")

  runeLongsword = Weapon("Rune Longsword", 40, 20, 0.1)

  arsidee = Player("Arsidee", 65, 45, 23, 30)
  arsidee.setWeapon(runeLongsword)

  goblin1 = Goblin()
  goblin2 = Goblin()
  goblin3 = Goblin()

  goblin1.physicalAttack(arsidee)
  goblin2.physicalAttack(arsidee)
  goblin3.physicalAttack(arsidee)

  arsidee.physicalAttack(goblin1)
  arsidee.physicalAttack(goblin2)
  arsidee.physicalAttack(goblin3)

  print("\n-- ACRYCE BATTLE --\n")

  archWizardStaff = Weapon("Arch Wizard Staff", 50, 99, 0.4)

  acryce = Player("Acryce", 256, 99, 99, 99)
  acryce.setWeapon(archWizardStaff)

  blackKnight = BlackKnight()

  robot = Robot()

  blackKnight.physicalAttack(acryce)
  robot.magicalAttack(acryce)

  acryce.magicalAttack(blackKnight)
  acryce.magicalAttack(robot)

if __name__ == '__main__':
  main()
