import csv
import re

def main():
  #lines = convertToStrings()
  #getStringsFrom(lines)
  # lines = ['a', 'b', 'c', 'd']
  lines = [
    ['John', 'Doe', '25'],
    ['Jane', 'Doe', '23'],
    ['Chad', 'Smith', '31'],
  ]
  dothething(lines)

def convertToStrings():
  f = open("input.txt", "r")
  lines = f.readlines()
  f.close()
  l = []
  for line in lines:
    l.append(line)
  f.close()
  return l

def getStringsFrom(l):
  regex = '^From\s'
  from_list = []
  for line in l:
      match = re.search(regex, line)
      if match:
        from_list.append(line)
        #print(line)
  return from_list

def dothething(list):
  with open('output.csv', 'w') as new_file:
      csv_writer = csv.writer(new_file, delimiter=',')
      for line in list:
        csv_writer.writerow(line)
      #From cwen@iupui.edu Thu Jan  3 16:29:07 2008

if __name__ == '__main__':
  main()
