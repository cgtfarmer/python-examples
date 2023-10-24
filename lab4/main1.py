import csv
import re

#def main():
  #f = open("input.txt", "r")
  #lines = f.readlines()
  #f.close()
  #l= []
  #for line in lines:
    #l.append(line)
    #print(l)
  #return l

def main():
  lines = convertToStrings()
  getStringsFrom(lines)

def convertToStrings():
  f = open("input.txt", "r")
  lines = f.readlines()
  f.close()
  l = []
  for line in lines:
    l.append(line)
    # print(l)
  f.close()
  return l

def getStringsFrom(l):
  regex = '^From\s'
  from_list = []
  for line in l:
      match = re.search(regex, line)
      if match:
        from_list.append(line)
        # print(line)
  return from_list

# def dothething():

if __name__ == '__main__':
  main()
