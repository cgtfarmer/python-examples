
import re

def main():
  example1()

  example2()

  example3()

  example4()

  example5()

def example1():
  s = "Apple Orange Pear"

  if re.search("Orange", s):
    print("Yes")
  else:
    print("No")

def example2():
  s = "Apple Orange Pear"

  if re.search("^Orange", s):
    print("Yes")
  else:
    print("No")

def example3():
  s = "Apple Orange Pear"

  if re.search("Apple", s):
    print("Yes")
  else:
    print("No")

def example4():
  s = "Apple Orange Pear"

  if re.search("^Apple", s):
    print("Yes")
  else:
    print("No")

def example5():
  s = "Examples: Cat Dog Fish"

  words = s.split()

  print(words)
  print(f'{words[2]},{words[1]},{words[3]}')

if __name__ == '__main__':
  main()

