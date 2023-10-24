class Weapon:
  def __init__(self, name, damage, attackSpeed, requiredHands):
    self.name = name
    self.damage = damage
    self.attackSpeed = attackSpeed
    self.requiredHands = requiredHands

  def __str__(self):
    return f'{self.name} - DMG: {self.damage}, Speed: {self.attackSpeed}, Req. Hands: {self.requiredHands}'
