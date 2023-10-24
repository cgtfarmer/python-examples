class Character:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
    self.movementSpeed = 5
    self.weapon = None
    self.ability1 = None
    self.ability2 = None
    self.x = 0
    self.y = 0

  def setName(self, name):
    self.name = name

  def setHp(self, hp):
    self.hp = hp

  def setMovementSpeed(self, movementSpeed):
    self.movementSpeed = movementSpeed

  def setWeapon(self, weapon):
    self.weapon = weapon

  def setAbility1(self, ability):
    self.ability1 = ability

  def setAbility2(self, ability):
    self.ability2 = ability

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def move(self, direction):
    if direction == "up":
      self.setY(self.y + self.movementSpeed)
    elif direction == "down":
      self.setY(self.y - self.movementSpeed)
    elif direction == "left":
      self.setX(self.x - self.movementSpeed)
    elif direction == "right":
      self.setX(self.x + self.movementSpeed)
    else:
      raise Exception("Error: Invalid direction")

  def attack(self, character):
    print(f'{self.name} attacks {character.name} for {self.weapon.damage} damage')
    character.takeDamage(self.weapon.damage)

  def takeDamage(self, damage):
    self.hp = (self.hp - damage)

    print(f'{self.name} took {damage} damage. Health is now {self.hp}')

    if self.hp <= 0:
      self.die()

  def die(self):
    print(f'{self.name} died')

class Weapon:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

def main():
  rustyShortsword = Weapon("Rusty Shortsword", 1)
  excalibur = Weapon("Excalibur", 250)

  acryce = Character("Acryce", 100)
  arsidee = Character("Arsidee", 100)

  acryce.setWeapon(excalibur)
  arsidee.setWeapon(rustyShortsword)

  arsidee.attack(acryce)
  acryce.attack(arsidee)

if __name__ == '__main__':
  main()
