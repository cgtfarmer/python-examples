from weapon import Weapon

class Weirdsword(Weapon):
  def __init__(self, name, damage, attackSpeed, otherValue):
    super().__init__(name, damage, attackSpeed, 3)

    # self.__name = name
    # self.__damage = damage
    # self.__attackSpeed = attackSpeed
    # self.__requiredHands = 3
    self.__otherValue = otherValue

  # Breaks
  # def __str__(self):
  #   return f'{self.__name} - DMG: {self.__damage}, Speed: {self.__attackSpeed}, Req. Hands: {self.__requiredHands}, OtherVal: {self.__otherValue}'

  # Works
  def __str__(self):
    return f'{super().__str__()}, OtherVal: {self.__otherValue}'

  # Works (Uncomment Weapon#Getters)
  # def __str__(self):
  #   return f'{self.getName()} - DMG: {self.getDamage()}, Speed: {self.getAttackSpeed()}, Req. Hands: {self.getRequiredHands()}, OtherVal: {self.__otherValue}'

  # Works (Uncomment Weirdsword#PrivateVars
  # def __str__(self):
  #   return f'{self.__name} - DMG: {self.__damage}, Speed: {self.__attackSpeed}, Req. Hands: {self.__requiredHands}, OtherVal: {self.__otherValue}'
