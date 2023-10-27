from character import Character

class Player(Character):
  def __init__(self, name, hp, strength, defense, critChance):
    super().__init__(name, hp, strength, defense)

    self.__critChance = critChance

  def getCritChance(self):
    return self.__critChance

  def setCritChance(self, critChance):
    self.__critChance = critChance

  def calculateDmg(self):
    return super().getStrength()

  def __str__(self):
    return f'{super().__str__()}, critChance={self.__critChance}'
