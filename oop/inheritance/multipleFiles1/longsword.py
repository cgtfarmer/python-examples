from weapon import Weapon

class Longsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 1)
