class Weapon:
  def __init__(self, name, damage, attackSpeed, requiredHands):
    self.name = name
    self.damage = damage
    self.attackSpeed = attackSpeed
    self.requiredHands = requiredHands

  def __str__(self):
    return f'{self.name} - DMG: {self.damage}, Speed: {self.attackSpeed}, Req. Hands: {self.requiredHands}'

class Longsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 1)

class Greatsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 2)

def main():
  longsword = Longsword("Steel Longsword", 10, 5)

  greatsword = Greatsword("Adamant Greatsword", 28, 2)

  print(longsword)
  print(greatsword)

if __name__ == '__main__':
  main()
