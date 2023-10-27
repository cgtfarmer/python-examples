class Player:
  def __init__(self, name, hp, strength, defense, critChance):
    self.__name = name
    self.__hp = hp
    self.__strength = strength
    self.__defense = defense
    self.__critChance = critChance

  def getName(self):
    return self.__name

  def getHp(self):
    return self.__hp

  def getStrength(self):
    return self.__strength

  def getDefense(self):
    return self.__defense

  def getCritChance(self):
    return self.__critChance

  def setName(self, name):
    self.__name = name

  def setHp(self, hp):
    self.__hp = hp

  def setStrength(self, strength):
    self.__strength = strength

  def setDefense(self, defense):
    self.__defense = defense

  def setCritChance(self, critChance):
    self.__critChance = critChance

  def calculateDmg(self):
    return self.__strength

  def __str__(self):
    return f'{self.__name}: hp={self.__hp}, strength={self.__strength}, defense={self.__defense}, critChance={self.__critChance}'
