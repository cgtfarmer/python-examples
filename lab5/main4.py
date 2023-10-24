import os.path
import csv
import re

def main():
  inputFilepath = getUserInput_inputFilepath()
  outputFilepath = getUserInput_outputFilepath()
  lines = getFileLinesAsList(inputFilepath)

  values = extractValues(lines)

  writeValuesToCsv(outputFilepath, values)

def getUserInput_inputFilepath():
  while True:
    fileName = input('Input file name: ').strip()
    filepath = f'files{os.sep}{fileName}'

    try:
      with open(filepath) as input_file:
        break
    except FileNotFoundError:
      print('File does not exist!')

  return filepath

def getUserInput_outputFilepath():
  input_prompt = 'Output file name: '
  validResponses = ['y', 'n']

  while True:
    csv_name = input(input_prompt).strip()
    csv_path = f'files{os.sep}{csv_name}'

    if os.path.isfile(csv_path):
      overwriteFileResponse = input('Overwrite existing file (y/n): ').strip().lower()

      while overwriteFileResponse not in validResponses:
        overwriteFileResponse = input('Enter (y/n): ').strip().lower()

      if overwriteFileResponse == 'n':
        input_prompt = 'New output file name: '
        continue

      if overwriteFileResponse == 'y':
        break

    return csv_path

def getFileLinesAsList(filepath):
  f = open(filepath, "r")
  lines = f.readlines()
  f.close()

  return lines

def extractValues(lines):
  values = []

  entry = {}
  for line in lines:
    if isEmailLine(line):
      entry['email'] = extractEmailFromLine(line)

    if isTimeLine(line):
      entry['time'] = extractTimeFromLine(line)

    if isConfidenceLine(line):
      entry['confidence'] = extractConfidenceFromLine(line)
      values.append(entry)
      entry = {}

  return values

def isEmailLine(line):
  return re.match('^From:\s', line)

def isTimeLine(line):
  return re.match('^X-DSPAM-Processed:\s', line)

def isConfidenceLine(line):
  return re.match('^X-DSPAM-Confidence:\s', line)

def extractEmailFromLine(line):
  return line[6:-1]

def extractTimeFromLine(line):
  if line[30] == '0':
    return line[31:-6]

  return line[30:-6]

def extractConfidenceFromLine(line):
  return line[20:-1]

def writeValuesToCsv(filepath, values):
  with open(filepath, 'w') as output_file:
    csvWriter = csv.writer(output_file)

    csvWriter.writerow(['Email', 'Time', 'Confidence'])

    for value in values:
      csvWriter.writerow([value['email'], value['time'], value['confidence']])

    try:
      test_for_zero(values, csvWriter)
    except ZeroDivisionError:
      print('No values present.')
    else:
      print('Data stored!')

def test_for_zero(values, csvWriter):
  confidence_list = []
  for entry in values:
    confidenceFloat = float(entry['confidence'])
    confidence_list.append(confidenceFloat)

  if len(confidence_list) == 0:
    raise ZeroDivisionError

  average_confidence = sum(confidence_list) / len(confidence_list)
  csvWriter.writerow(['', 'Average', f'{average_confidence:.4f}'])

if __name__ == '__main__':
  main()
