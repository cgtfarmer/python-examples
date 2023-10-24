class Person:
  def __init__(self, firstName, lastName, age, weight, admin):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.weight = weight
    self.admin = admin

def main():
  example1()

  example2()

def example1():
  people = [
    { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True },
    { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 152.2, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 12, "weight": 91.7, "admin": False }
  ]

  for person in people:
    print(f'{person["firstName"]} {person["lastName"]} is {person["age"]} years old')

def example2():
  people = [
    Person("John", "Doe", 28, 185.3, False),
    Person("Jane", "Doe", 25, 143.7, True),
    Person("Chad", "Doe", 15, 152.2, True),
    Person("Karen", "Doe", 12, 91.7, False),
  ]

  for person in people:
    print(f'{person.firstName} {person.lastName} is {person.age} years old')

if __name__ == '__main__':
  main()
