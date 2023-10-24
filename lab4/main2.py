import csv
import re


def main():
    lines = convertToStrings()
    from_space_list = getStringsFrom(lines)
    from_colon_list = getStringsFromColon(lines)
    listToSend = rearrangelist(from_space_list)
    writeToCsvFile(listToSend)


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
    from_space_list = []
    for line in l:
        match = re.search(regex, line)
        if match:
            from_space_list.append(line)
            # print(line)
    return from_space_list


def getStringsFromColon(l):
    regex = '^From:'
    fromColon_list = []
    for line in l:
        match = re.search(regex, line)
        if match:
            fromColon_list.append(line)
            # print(line)
    return fromColon_list


# def emailCount():
# with open('output.txt' 'w') as new_file:
# for line in new_file:

def rearrangelist(from_space_list):
    finalList = []
    for string in from_space_list:
        stringToSend = string.split()[1:]
        newstringToSend = [stringToSend[0],stringToSend[1],stringToSend[3],stringToSend[2],stringToSend[5],stringToSend[4]]
        finalList.append(newstringToSend)
        #print(finalList)
        #print(newstringToSend)
        # email, weekday, month, number, time, year
        # needs to be
        # email, weekday, month, number, year, time
    return finalList

def writeToCsvFile(listToSend):
    with open('output.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=",")
        header_list = ['Email', 'Day', 'Date', 'Month', 'Year', 'Time']
        #'Email', 'Day', 'Date', 'Month', 'Year', 'Time')
        csv_writer.writerow(header_list)
        csv_writer.writerows(listToSend)



if __name__ == '__main__':
    main()
