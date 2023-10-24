def main():
  people = [
    { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False },
    { "firstName": "Jane", "lastName": "Doe", "age": 23, "weight": 153.7, "admin": False },
    { "firstName": "Chad", "lastName": "Smith", "age": 28, "weight": 215.6, "admin": True },
    { "firstName": "Karen", "lastName": "Smith", "age": 27, "weight": 178.1, "admin": False }
  ]
  # people = loadPeopleFromHardCodedListOfDicts()
  # people = loadPeopleFromCsv()
  # people = loadPeopleFromDatabase()
  # people = loadPeopleFromApi()

  print(people[0]["firstName"]) # String
  print(people[0]["lastName"]) # String
  print(people[0]["age"]) # Int
  print(people[0]["weight"]) # Float
  print(people[0]["admin"]) # Boolean

  firstPerson = people[0]
  print(firstPerson["firstName"])
  print(firstPerson["lastName"])
  print(firstPerson["age"])
  print(firstPerson["weight"])
  print(firstPerson["admin"])

  i = 0
  while i < len(people):
    person = people[i]

    print("---")
    print(person["firstName"])
    print(person["lastName"])
    print(person["age"])
    print(person["weight"])
    print(person["admin"])

    i = (i + 1)

  print("---\nDone!")

if __name__ == '__main__':
  main()
