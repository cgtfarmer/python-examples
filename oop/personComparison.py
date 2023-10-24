class Person:
  def __init__(self, firstName, lastName, age):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age

def main():
  # Representing a single entity across disparate variables
  # (This is bad)
  firstName = "John"
  lastName = "Doe"
  age = 25

  print("\n1 ---")
  print(firstName)
  print(lastName)
  print(age)

  # Representing a single entity using a "compound variable" (a dict)
  # (This is acceptable, but it doesn't enable type-safety and
  # doesn't allow for adding behavior to the entity)
  person = { "firstName": "John", "lastName": "Doe", "age": 25 }

  print("\n2 ---")
  print(person["firstName"])
  print(person["lastName"])
  print(person["age"])

  # Representing a single entity using a Person object, which
  # is constructed from the Person class
  awesomePerson = Person("John", "Doe", 25)

  print("\n3 ---")
  print(awesomePerson.firstName)
  print(awesomePerson.lastName)
  print(awesomePerson.age)

if __name__ == '__main__':
  main()
