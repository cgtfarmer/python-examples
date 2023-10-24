import csv

def main():
  users = loadCsv('userData.csv')

  totalWeight = sumWeights(users)
  avgWeight = (totalWeight / len(users))

  print(f'Total Weight: {totalWeight}')
  print(f'Avg Weight: {avgWeight}')

def sumWeights(users):
  totalWeight = 0

  for user in users:
    totalWeight = (totalWeight + float(user["weight"]))

  return totalWeight

def loadCsv(filepath):
  entries = []

  with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    for entry in reader:
      entries.append(entry)

  return entries

if __name__ == '__main__':
  main()
