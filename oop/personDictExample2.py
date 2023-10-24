def main():
  boring()
  interesting()

def boring():
  value = -5

  if value > 0:
    print("Positive")
  elif value < 0:
    print("Negative")
  else:
    print("Is Zero")

def interesting():
  person = { "firstName": "John", "lastName": "Doe", "age": 25, "weight": 185.3, "admin": False }

  if person["age"] <= 18:
    print("Minor")
  elif person["age"] <= 60:
    print("Adult")
  else:
    print("Senior")

if __name__ == '__main__':
  main()
