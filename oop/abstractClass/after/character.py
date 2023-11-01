from abc import ABC, abstractmethod

class Character(ABC):

  @abstractmethod
  def __init__(self, name, hp, strength, defense):
    self.__name = name
    self.__hp = hp
    self.__strength = strength
    self.__defense = defense

  def getName(self):
    return self.__name

  def getHp(self):
    return self.__hp

  def getStrength(self):
    return self.__strength

  def getDefense(self):
    return self.__defense

  def setName(self, name):
    self.__name = name

  def setHp(self, hp):
    self.__hp = hp

  def setStrength(self, strength):
    self.__strength = strength

  def setDefense(self, defense):
    self.__defense = defense

  @abstractmethod
  def calculateDmg(self):
    pass

  def __str__(self):
    return f'{self.__name}: hp={self.__hp}, strength={self.__strength}, defense={self.__defense}'
