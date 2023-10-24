class Weapon:
  def __init__(self, name, damage, attackSpeed, requiredHands):
    self.name = name
    self.damage = damage
    self.attackSpeed = attackSpeed
    self.requiredHands = requiredHands

  def describe(self):
    print(f'{self.name} - DMG: {self.damage}, Speed: {self.attackSpeed}, Req. Hands: {self.requiredHands}')

class Longsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 1)

class Greatsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 2)

def main():
  longsword = Longsword("Steel Longsword", 10, 5)

  greatsword = Greatsword("Adamant Greatsword", 28, 2)

  longsword.describe()

  greatsword.describe()

if __name__ == '__main__':
  main()
