# from utilities import *
import sys
import math

def main():
  print("Yay!")

  # print(sys.argv)

  # values = ['meow.py', 'a', 'b', 'c']
  # values = sys.argv
  values = ['meow.py', '5.3872', '3.1255', '7.933']

  # supposedInts = values[1:]
  supposedFloats = values[1:]

  # print(supposedInts)
  # print(supposedInts[0])
  # print(supposedInts[1])
  # print(supposedInts[2])

  # print(type(supposedInts[0]))
  # print(int(supposedInts[0]) * int(supposedInts[2]))

  # actualInts = convertStringsToIntegers(supposedInts)
  # actualInts = convertStringsToFloats(supposedFloats)
  actualInts = convertStringsToTruncatedFloats(supposedFloats)
  print(actualInts)

  print("Doing new magical things for the next piece of functionality")
  print("Doing new magical things for the next piece of functionality")
  print("Doing new magical things for the next piece of functionality")

def convertStringsToTruncatedFloats(supposedFloats):
  actualFloats = []

  i = 0
  while i < 3:
    print(supposedFloats[i])

    truncatedFloatString = truncateFloatString(supposedFloats[i])

    actualFloatValue = float(truncatedFloatString)

    actualFloats.append(actualFloatValue)

    i = (i + 1)

  print(actualFloats)
  return actualFloats

def convertStringsToFloats(supposedFloats):
  actualFloats = []

  i = 0
  while i < 3:
    print(supposedFloats[i])

    actualFloatValue = float(supposedFloats[i])

    actualFloats.append(actualFloatValue)

    i = (i + 1)

  print(actualFloats)
  return actualFloats

def truncateFloatString(floatString):
  actualFloatValue = float(floatString)

  truncatedFloatString = f"{actualFloatValue:.2f}"

  return truncatedFloatString

def convertStringsToIntegers(supposedInts):
  actualInts = []

  i = 0
  while i < 3:
    print(supposedInts[i])

    actualInts.append(int(supposedInts[i]))

    i = (i + 1)

  print(actualInts)
  return actualInts

if __name__ == "__main__":
  main()
