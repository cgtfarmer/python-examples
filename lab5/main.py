import os.path
import csv
import re

def main():
  email_list = []
  time_list = []
  confidence_list = []
  filepath = getInputFilepathUserInput()
  csv_path = getOutputFilepathUserInput()
  lines = getFileLinesAsList(filepath)

  with open(csv_path, 'w') as output_file:
    csvWriter = csv.writer(output_file)

    for line in lines:
      if re.match('^From:\s', line):
        email_list.append(line[6:-1])

      if re.match('^X-DSPAM-Processed:\s', line):
        time_list.append(line[30:-6])

      if re.match('^X-DSPAM-Confidence:\s', line):
        confidence_list.append(line[20:-1])

    for i in range(len(email_list)):
      confidence_list[i] = float(confidence_list[i])

      if time_list[i][0] == '0':
        time_list[i] = time_list[i][1:]

    csvWriter.writerow(['Email', 'Time', 'Confidence'])

    for i in range(len(email_list)):
      csvWriter.writerow([email_list[i],time_list[i],confidence_list[i]])

    try:
      test_for_zero(confidence_list, csvWriter)
    except ZeroDivisionError:
      print('No values present.')
    else:
      print('Data stored!')

def getFileLinesAsList(filepath):
  f = open(filepath, "r")
  lines = f.readlines()
  f.close()

  return lines

def getInputFilepathUserInput():
  while True:
    fileName = input('Input file name: ').strip()
    filepath = f'files{os.sep}{fileName}'

    try:
      with open(filepath) as input_file:
        break
    except FileNotFoundError:
      print('File does not exist!')

  return filepath

def getOutputFilepathUserInput():
  input_prompt = 'Output file name: '
  validResponses = ['y', 'n']

  while True:
    csv_name = input(f'{input_prompt}').strip()
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

def test_for_zero(confidence_list, csvWriter):
  if len(confidence_list) == 0:
    raise ZeroDivisionError

  average_confidence = sum(confidence_list) / len(confidence_list)
  csvWriter.writerow(['', 'Average', f'{average_confidence:.4f}'])

if __name__ == '__main__':
  main()
