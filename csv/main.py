import csv
import random

def main():
  firstNames = getFileLinesAsList("firstNames.txt")
  lastNames = getFileLinesAsList("lastNames.txt")

  filepath = 'output.csv'
  fullNames = generateRandomFullNames(firstNames, lastNames)

  data = addAgeData(fullNames)
  data = addWeightData(data)
  data = addGenderData(data)
  data = addSmokerData(data)
  data = addIdData(data)

  headers = ['id', 'firstName', 'lastName', 'age', 'weight', 'gender', 'smoker']
  writeListToCsvFile(filepath, headers, fullNames)

def addAgeData(data):
  for datum in data:
    choice = random.randint(1, 110)
    datum.append(choice)

  return data

def addWeightData(data):
  for datum in data:
    choice = random.randint(800, 2800)
    floatChoice = (choice / 10.0)
    datum.append(floatChoice)

  return data

def addGenderData(data):
  for datum in data:
    choice = random.randint(0, 1)

    if choice == 0:
      datum.append("M")
    else:
      datum.append("F")

  return data

def addSmokerData(data):
  for datum in data:
    choice = random.randint(0, 4)

    if choice <= 3:
      datum.append("False")
    else:
      datum.append("True")

  return data

def addIdData(data):
  for i in range(len(data)):
    data[i].insert(0, str(i + 1))

  return data

def writeListToCsvFile(filepath, headers, values):
  with open(filepath, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    csv_writer.writerows(values)

def generateRandomFullNames(firstNames, lastNames):
  names = []
  for i in range(2500):
    firstName = sanitizeName(selectRandomElement(firstNames))
    lastName = sanitizeName(selectRandomElement(lastNames))

    # names.append({ "firstName": firstName, "lastName": lastName })
    names.append([firstName, lastName])

  return names

def sanitizeName(name):
  return name.strip().capitalize()

def selectRandomElement(values):
  lastElementIndex = (len(values) - 1)
  choiceIndex = random.randint(0, lastElementIndex)

  return values[choiceIndex]

def getFileLinesAsList(filename):
  f = open(filename, "r")
  lines = f.readlines()
  f.close()

  return lines

if __name__ == '__main__':
  main()
