
def main():
  example1()

  example2()

def example1():
  firstName = "John"
  lastName = "Doe"
  age = 25
  weight = 185.3
  admin = False

  print(age)

def example2():
  person = { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False }

  print(person["age"])

def example3():
  firstName1 = "John"
  lastName1 = "Doe"
  age1 = 25
  weight1 = 185.3
  admin1 = False

  firstName2 = "Jane"
  lastName2 = "Doe"
  age2 = 23
  weight2 = 143.7
  admin2 = True

  print(age1)
  print(age2)

def example4():
  person1 = { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False }

  person2 = { "firstName": "Jane", "lastName": "Doe", "age": 23, "weight": 143.7, "admin": True }

  print(person1["age"])
  print(person2["age"])

if __name__ == '__main__':
  main()
