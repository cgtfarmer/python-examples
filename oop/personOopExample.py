class Person:
  def __init__(self, firstName, lastName, age):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age

  def greet(self):
    print(f'Hello, my name is {self.firstName} {self.lastName}, and I am {self.age} years old.')

  def speak(self, text):
    print(f'{self.firstName} says: {text}')

  def getOneYearOlder(self):
    self.age = (self.age + 1)

def main():
  person = Person("John", "Doe", 25)

  person.greet()

  person.speak("I'm a cat")

  person.getOneYearOlder()

  person.greet()

if __name__ == '__main__':
  main()
