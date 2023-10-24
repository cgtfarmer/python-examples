
def main():
  values1 = ['a', 'b', 'c']
  values2 = ['a', 'b', 'c', 'd', 'e']
  values3 = ['e', 'd', 'c', 'b', 'a']

  one(values1)
  one(values2)
  one(values3)

  two(values1)
  two(values2)
  two(values3)

  three(values1)
  three(values2)
  three(values3)

  four(values1)
  four(values2)
  four(values3)

  five(values1)
  five(values2)
  five(values3)

  six(values1)
  six(values2)
  six(values3)

  seven(values1)
  seven(values2)
  seven(values3)

  eight(values1)
  eight(values2)
  eight(values3)

  nine(values1)
  nine(values2)
  nine(values3)

def one(values):
  for value in values:
    print(value)

def two(values):
  for i in range(len(values)):
    print(values[i])

def three(values):
  for i in range(len(values)):
    value = values[i]
    print(value)

def four(values):
  for value in values:
    if value == 'a':
      return value

def five(values):
  for i in range(len(values)):
    if values[i] == 'a':
      return values[i]

def six(values):
  for i in range(len(values)):
    value = values[i]
    if value == 'a':
      return value

def seven(values):
  for value in values:
    if value == 'e':
      return value

def eight(values):
  for i in range(len(values)):
    if values[i] == 'e':
      return values[i]

def nine(values):
  for i in range(len(values)):
    value = values[i]
    if value == 'e':
      return value

if __name__ == '__main__':
  main()
