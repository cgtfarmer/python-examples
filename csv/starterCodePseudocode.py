
def mainPseudocode():
  # Load user data

  # Sum weights

  # Compute avg weight

  # Print total and average weights

  return

def main():
  # Load user data
  users = loadCsv('userData.csv')

  # Sum weights
  totalWeight = sumWeights(users)

  # Compute avg weight
  avgWeight = (totalWeight / len(users))

  # Print total and average weights
  print(f'Total Weight: {totalWeight}')
  print(f'Avg Weight: {avgWeight}')

def main2():
  # Load user data
  users = []

  with open('userData.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for entry in reader:
      users.append(entry)

  # Sum weights
  totalWeight = 0

  for user in users:
    totalWeight = (totalWeight + float(user["weight"]))

  # Compute avg weight
  avgWeight = (totalWeight / len(users))

  # Print total and average weights
  print(f'Total Weight: {totalWeight}')
  print(f'Avg Weight: {avgWeight}')

def main():
  # Load user data
  users = loadCsv('userData.csv')

  # Sum weights
  totalWeight = sumWeights(users)

  # Compute avg weight
  avgWeight = computeAvgWeight(totalWeight, users)

  # Print total and average weights
  print(f'Total Weight: {totalWeight}')
  print(f'Avg Weight: {avgWeight}')

def computeAvgWeight(totalWeight, users):
  return (totalWeight / len(users))

def computeAvgWeight2(totalWeight, totalUsers):
  return (totalWeight / totalUsers)

def computeAvg(valueSum, units):
  return (valueSum / units)

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
