import os.path
import csv
import re
def main():
    email_list = []
    time_list = []
    confidence_list = []
    file_path = selectInputFile()
    csv_path = provideCSVpath()
    with open(file_path, 'r') as file:
        with open(csv_path, 'w') as output_file:
            write_to_csv = csv.writer(output_file)
            for line in file:
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
            write_to_csv.writerow(['Email', 'Time', 'Confidence'])
            for i in range(len(email_list)):
                write_to_csv.writerow([email_list[i],time_list[i],confidence_list[i]])
            try:
                test_for_zero(confidence_list, write_to_csv)
            except ZeroDivisionError:
                print('No values present.')
            else:
                print('Data stored!')

def selectInputFile():
  while True:
    try:
      file_path = 'files/' + input('Input file name: ').strip()
      with open(file_path) as input_file:
        break
    except FileNotFoundError:
      print('File does not exist!')
  return file_path
def provideCSVpath():
  input_prompt = 'Output file name: '
  while True:
    csv_name = input(f'{input_prompt}').strip()
    csv_path = 'files' + os.sep + csv_name

    if os.path.isfile(csv_path):
      overwritefile = input('Overwrite existing file (y/n): ').strip().lower()
      while overwritefile != 'y' and overwritefile != 'n':
        overwritefile = input('Enter (y/n): ').strip().lower()
      if overwritefile == 'n':
        input_prompt = 'New output file name: '
        continue
      elif overwritefile == 'y':
        return csv_path
    return csv_path
def test_for_zero(confidence_list, write_to_csv):
    if len(confidence_list) == 0:
        raise ZeroDivisionError
    average_confidence = sum(confidence_list) / len(confidence_list)
    write_to_csv.writerow(['', 'Average', f'{average_confidence:.4f}'])

if __name__ == '__main__':
  main()
