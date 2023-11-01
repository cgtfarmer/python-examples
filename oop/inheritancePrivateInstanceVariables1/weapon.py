class Weapon:
  def __init__(self, name, damage, attackSpeed, requiredHands):
    self.__name = name
    self.__damage = damage
    self.__attackSpeed = attackSpeed
    self.__requiredHands = requiredHands

  def getName(self):
    return self.__name

  def getDamage(self):
    return self.__damage

  def getAttackSpeed(self):
    return self.__attackSpeed

  def getRequiredHands(self):
    return self.__requiredHands

  def __str__(self):
    return f'{self.__name} - DMG: {self.__damage}, Speed: {self.__attackSpeed}, Req. Hands: {self.__requiredHands}'
