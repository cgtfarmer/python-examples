import sys
def add(values):
    values = convertStringsToFloats(values)
    list_sum = 0.00
    for i in values:
        if i < 0:
            list_sum += i
    return f"Answer is {list_sum:.2f}"
def subtract(values):
    values = convertStringsToFloats(values)
    list_diff = 0
    if values[0] >= 0:
        list_diff = values[0]
        for i in range(1, len(values)):
            if values[i] > 0:
                list_diff -= values[i]
            else:
                 pass
    return f'Answer is {list_diff:.2f}'
def multiply(values):
    values = convertStringsToFloats(values)
    result = 1
    for i in values:
        if i != 0:
            result = result * i
        else:
            pass
    return f'Answer = {result:.2f}'

def divide(values):
    values = convertStringsToFloats(values)
    if 0 in values[1:]:
        print('Cannot divide by 0.')
        sys.exit()
    elif values[0] == 0:
        list_quo = 0
    else:
        list_quo = values[0]
        for i in values[1:]:
            list_quo /= i
    return f'Answer is {list_quo:.2f}'

def convertStringsToFloats(values):
  actualFloats = []

  for i in range(len(values)):
    #print(values[i])

    stringValue = values[i]

    floatValue = float(stringValue)

    truncatedValue = f'{floatValue:.2f}'

    truncatedFloatValue = float(truncatedValue)

    actualFloats.append(truncatedFloatValue)
  #print(actualFloats)
  return actualFloats