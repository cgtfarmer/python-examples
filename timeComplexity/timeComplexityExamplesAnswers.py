
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

"""
  Worst: n
  Best: n
  Avg: n
"""
def one(values):
  for value in values:
    print(value)

"""
  Worst: n
  Best: n
  Avg: n
"""
def two(values):
  for i in range(len(values)):
    print(values[i])

"""
  Worst: n
  Best: n
  Avg: n
"""
def three(values):
  for i in range(len(values)):
    value = values[i]
    print(value)

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def four(values):
  for value in values:
    if value == 'a':
      return value

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def five(values):
  for i in range(len(values)):
    if values[i] == 'a':
      return values[i]

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def six(values):
  for i in range(len(values)):
    value = values[i]
    if value == 'a':
      return value

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def seven(values):
  for value in values:
    if value == 'e':
      return value

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def eight(values):
  for i in range(len(values)):
    if values[i] == 'e':
      return values[i]

"""
  Worst: n
  Best: 1
  Avg: (n / 2)
"""
def nine(values):
  for i in range(len(values)):
    value = values[i]
    if value == 'e':
      return value

if __name__ == '__main__':
  main()
