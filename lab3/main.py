
import csv
import re

def main():
  f = open("input.txt", "r")
  lines = f.readlines()
  f.close()

  i = 0
  while i < len(lines):
    line = lines[i].strip()

    if re.search("^From ", line):
      print(line)

    i = (i + 1)

  # with open('input.txt', newline='') as csvfile:
  #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

if __name__ == '__main__':
  main()
