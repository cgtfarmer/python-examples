# from utilities import *
import sys

def main():
  print("Yay!")

  # print(sys.argv)

  # values = ['meow.py', 'a', 'b', 'c']
  # values = sys.argv
  values = ['meow.py', '5', '3', '7']

  supposedInts = values[1:]

  # print(supposedInts)
  # print(supposedInts[0])
  # print(supposedInts[1])
  # print(supposedInts[2])

  # print(type(supposedInts[0]))
  # print(int(supposedInts[0]) * int(supposedInts[2]))

  actualInts = []
  i = 0
  while i < 3:
    print(supposedInts[i])

    actualInts.append(int(supposedInts[i]))

    i = (i + 1)

  print(actualInts)

if __name__ == "__main__":
  main()
