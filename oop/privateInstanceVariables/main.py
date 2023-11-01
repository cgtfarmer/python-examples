from person import Person

def main():
  # example1()
  # example2()
  example3()

def example3():
  people = loadPeople()

  printCollection(people)

  agePeople(people)

  printCollection(people)

def loadPeople():
  p1 = Person('John', 'Doe', 25)
  p2 = Person('Jane', 'Doe', 23)
  p3 = Person('Chad', 'Smith', 27)
  p4 = Person('Karen', 'Smith', 26)

  people = [p1, p2, p3, p4]
  return people

def agePeople(people):
  for person in people:
    person.ageOneYear()

def printCollection(collection):
  if collection == None:
    raise Exception('Requires collection to be present')

  for entry in collection:
    print(entry)

  print('--- Everyone got older ---')

def example2():
  p1 = Person('John', 'Doe', 25)

  p2 = Person('Jane', 'Smith', 23)

  print(p1)
  print(p2)

  print('--- Everyone got older ---')

  # p1.setAge(26)
  # p2.setAge(24)

  # p1.setAge(p1.getAge() + 1)
  # p2.setAge(p2.getAge() + 1)

  p1.ageOneYear()
  p2.ageOneYear()

  print(p1)
  print(p2)

def example1():
  p1 = Person('John', 'Doe', 25)

  p2 = Person('Jane', 'Smith', 23)

  print(p1)
  print(p2)

  # print(p1.getFirstName())
  # print(p2.getFirstName())

  print(f'Hello, {p1.getFirstName()} {p1.getLastName()}, how are you?')
  print(f'Hello, {p2.getFirstName()} {p2.getLastName()}, how are you?')

  # print(f'Hello, {p1.getFullName()}, how are you?')
  # print(f'Hello, {p2.getFullName()}, how are you?')

if __name__ == '__main__':
  main()
