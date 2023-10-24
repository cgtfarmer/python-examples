from weapon import Weapon

class Greatsword(Weapon):
  def __init__(self, name, damage, attackSpeed):
    super().__init__(name, damage, attackSpeed, 2)
