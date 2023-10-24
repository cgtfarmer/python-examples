
class Player:
  def __init__(self, name, level, hp, strength, magic):
    self.name = name
    self.level = level
    self.hp = hp
    self.strength = strength
    self.magic = magic

  def __str__(self):
    return f'{self.name}) lvl={self.level}, hp={self.hp} strength={self.strength}, magic={self.magic}'

class Weapon:
  def __init__(self, name, strength, magic, critChance):
    self.name = name
    self.strength = strength
    self.magic = magic
    self.critChance = critChance

  def __str__(self):
    return f'{self.name}) strength={self.strength}, magic={self.magic}, critChance={self.critChance}'

def main():
  person1 = Player('Acryce', 99, 99, 99, 99)

  person2 = Player('Arsidee', 45, 30, 41, 22)

  weapon1 = Weapon('Club', 10, 10, 0.3)

  weapon2 = Weapon('Adamant Longsword', 20, 30, 0.15)

  print(person1)
  print(person2)
  print(weapon1)
  print(weapon2)

if __name__ == '__main__':
  main()
