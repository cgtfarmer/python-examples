import os.path
import csv
import re
def main():
  file_path = selectInputFile()
  csv_path = provideCSVpath()
  lines = readFileToList(file_path)
  filtered_list = list_filter(lines)
  # with open(file_path, "r") as f:
  #   with open(csv_path, 'w', newline='')as csv_file:
  #     csv_writer = csv.writer(csv_file, delimiter=",")
  #     header_list = ['Email','Time','Confidence']
  #     csv_writer.writerow(header_list)

  #print(from_colon_list)
  #print(csv_path)
  #print(file_path)
def selectInputFile():
  while True:
    try:
      file_path = 'files/' + input('Input file name: ').strip()
      with open(file_path) as input_file:
        break
    except FileNotFoundError:
      print('File does not exist!')
  #print(file_path)
  return file_path
def provideCSVpath():
  input_prompt = 'Output file name: '
  while True:
    csv_name = input(f'{input_prompt}').strip()
    csv_path = 'files/' + os.sep + csv_name

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

def readFileToList(file_name):
  with open(file_name, "r") as f:
    lines = f.readlines()
    ##read file and creates list##
  return lines
def list_filter(lines):
  from_colon_list_of_lists = []
  from_colon_list = []
  datetime_list =[]
  time_list = []
  confidence_list_of_lists = []
  confidence_list = []
  listToSend = []
  regex = '^From:'
  regex2 = '^X-DSPAM-Processed'
  regex3 = '^X-DSPAM-Confidence:'
  i = 0
  p = 0
  d = 0
  for line in lines:
      match = re.search(regex, line)
      if match:
          from_colon_list_of_lists.append(line.split()[1:])
  for line in lines:
      match = re.search(regex2, line)
      if match:
          datetime_list.append(line.split()[1:])
  for line in lines:
      match = re.search(regex3, line)
      if match:
          confidence_list_of_lists.append(line.split()[1:])
  for time in datetime_list:
      time = datetime_list[i][3]
      time_list.append(time)
      i = (i + 1)
  for email in from_colon_list_of_lists:
      email = from_colon_list_of_lists[d][0]
      from_colon_list.append(email)
      d = d + 1

  for confidence in confidence_list_of_lists:
      confidence = confidence_list_of_lists[p][0]
      confidence_list.append(confidence)
      p = (p + 1)

  #print(datetime_list)
  #print(time_list)
  print(from_colon_list)
  #print(confidence_list)
if __name__ == '__main__':
  main()
