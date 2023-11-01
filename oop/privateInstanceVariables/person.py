class Person:
  def __init__(self, firstName, lastName, age):
    self.__firstName = firstName
    self.__lastName = lastName
    self.__age = age

  def getFirstName(self):
    return self.__firstName

  def getLastName(self):
    return self.__lastName

  def getFullName(self):
    return f'{self.__firstName} {self.__lastName}'

  def getAge(self):
    return self.__age

  def setAge(self, age):
    self.__age = age

  def ageOneYear(self):
    self.__age = (self.__age + 1)

  def __str__(self):
    return f'{self.__firstName} {self.__lastName}: {self.__age}'
