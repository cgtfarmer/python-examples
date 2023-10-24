
"""
1. Dicts
2. Lists
3. Loops
4. Functions <-- This is gonna wait
"""
def main():
  people = [
    { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True },
    { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 143.7, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 12, "weight": 91.7, "admin": False }
  ]

def example1():
  firstName = "John"
  lastName = "Doe"
  age = 28
  weight = 185.3
  print(f"Hello, my name is {firstName} {lastName}, I am {age} years old, and I weigh {weight} lbs")

def example2():
  firstName = "John"
  lastName = "Doe"
  age = 28
  weight = 185.3
  print(f"Hello, my name is {firstName} {lastName}, I am {age} years old, and I weigh {weight} lbs")

  firstName2 = "Jane"
  lastName2 = "Doe"
  age2 = 25
  weight2 = 143.7
  print(f"Hello, my name is {firstName2} {lastName2}, I am {age2} years old, and I weigh {weight2} lbs")

def example3():
  person = { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False }

  print(f'Hello, my name is {person["firstName"]} {person["lastName"]}, I am {person["age"]} years old, and I weigh {person["weight"]} lbs')

  person2 = { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True }

  print(f'Hello, my name is {person2["firstName"]} {person2["lastName"]}, I am {person2["age"]} years old, and I weigh {person2["weight"]} lbs')

def example4():
  names = ["John", "Jane", "Chad", "Karen"]

  person = { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False }

  fakeList = { 0: "John", 1: "Jane", 2: "Chad", 3: "Karen" }

  ditty = { True: "Success", False: "Failure" }

  print(names[1])
  print(person["lastName"])
  print(fakeList[1])

  print("---")
  print(ditty[True])
  print(ditty[False])

  print("---")
  print(ditty[(5 > 3) and (3 < 2)])

def example5():
  person1 = { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False }

  person2 = { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True }

  person3 = { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 143.7, "admin": True }

  print(person1)
  print(person2)
  print(person3)

  identifyMinorOrAdult(person1)
  identifyMinorOrAdult(person2)
  identifyMinorOrAdult(person3)

def identifyMinorOrAdult(bruh):
  if (bruh["age"] < 18):
    print(f'{bruh["firstName"]} is a minor')
  else:
    print(f'{bruh["firstName"]} is an adult')

def example6():
  ages = [23, 28, 21, 15, 12, 35]

  # print(ages)
  print(ages[2])

  people = [
    { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True },
    { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 143.7, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 12, "weight": 91.7, "admin": False }
  ]

  # print(people)
  # print(people[2])
  # print(people[2]["lastName"])
  # print({ "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True }["lastName"])

  # print(people[0]["firstName"])
  # print(people[1]["firstName"])
  # print(people[2]["firstName"])
  # print(people[3]["firstName"])

  i = 0
  # while i < 4:
  while i < len(people):
    print(people[i]["firstName"])

    i = (i + 1)

def example7():
  people = [
    { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True },
    { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 143.7, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 12, "weight": 91.7, "admin": False }
  ]

  U_TOO_HEAVY = 500.5 # How many lbs b4 u 2 fat

  weight = 0.0
  i = 0
  while i < len(people):
    print(f'{people[i]["firstName"]} weighs {people[i]["weight"]} lbs')

    weight = (weight + people[i]["weight"])
    print(f'New total weight: {weight}\n')

    i = (i + 1)

  print(f'Final weight: {weight}')

  if weight > U_TOO_HEAVY:
    print("Y'all too fat, GTFO")
  else:
    print("K, u gud")

def example8():
  i = 0
  while i < 10:
    print("meow")

    i = (i + 1)

def example9():
  people = [
    { "firstName": "John", "lastName": "Doe", "age": 28, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 25, "weight": 143.7, "admin": True },
    { "firstName": "Chad", "lastName": "Smith", "age": 15, "weight": 143.7, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 12, "weight": 91.7, "admin": False }
  ]

  i = 0
  while i < len(people):
    # print(i)
    # print(people[i])
    if people[i]["admin"] == True:
      print(f'Hello {people[i]["firstName"]} {people[i]["lastName"]}, welcome to the admin portal!')
    else:
      print(f'Hello {people[i]["firstName"]} {people[i]["lastName"]}, you don\'t belong here')

    i = (i + 1)

if __name__ == '__main__':
  main()
