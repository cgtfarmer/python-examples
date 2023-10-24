def main():
  print("-- BEGIN --")

  print(createGreeting("John", "Doe"))

  print(createGreeting("Jane", "Doe"))

  print(createGreeting("Chad", "Doe"))

  print("-- END --")

def createGreeting(firstName, lastName):
  if (firstName == None) or (lastName == None):
    raise Exception("Params must be present")

  if (type(firstName) != str) or (type(lastName) != str):
    raise Exception("Params must be strings")

  if (firstName.strip() == "") or (lastName.strip() == ""):
    raise Exception("Params must not be empty strings")

  return f'Hello {firstName} {lastName}, welcome home!'

if __name__ == '__main__':
  main()
