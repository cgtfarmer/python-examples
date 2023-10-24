class Player:
  def __init__(self, firstName, lastName, xp):
    self.__firstName = firstName
    self.__lastName = lastName
    self.__xp = xp

  def getXp(self):
    return self.__xp

  def describe(self):
    print(f'{self.__firstName} {self.__lastName}: {self.__xp}')

  def __str__(self):
    return f'{self.__firstName} {self.__lastName}: {self.__xp}'
