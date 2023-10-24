
def main():
  example1()

  example2()

def example1():
  user = { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False }

  if (user['age'] > 0) and (user['age'] < 18):
    print(f'{user["firstName"]} is a minor')
  elif (user['age'] >= 18) and (user['age'] < 65):
    print(f'{user["firstName"]} is an adult')
  elif (user['age'] >= 65):
    print(f'{user["firstName"]} is a senior')

def example2():
  user = { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False }

  if isMinor(user):
    print(f'{user["firstName"]} is a minor')
  elif isAdult(user):
    print(f'{user["firstName"]} is an adult')
  elif isSenior(user):
    print(f'{user["firstName"]} is a senior')

def isMinor(user):
  return (user['age'] > 0) and (user['age'] < 18)

def isAdult(user):
  return (user['age'] >= 18) and (user['age'] < 65)

def isSenior(user):
  return (user['age'] >= 65)

if __name__ == '__main__':
  main()
