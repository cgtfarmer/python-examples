def main():
  fifth = { 'value': 'e', 'next': None }

  fourth = { 'value': 'd', 'next': fifth }

  third = { 'value': 'c', 'next': fourth }

  second = { 'value': 'b', 'next': third }

  first = { 'value': 'a', 'next': second }

  traverseLinkedList(first)

def traverseLinkedList(element):
  print(f'Current Element: {element["value"]}')

  if element['next'] == None:
    print("This is the final element, stopping.")
    return

  print("Going to next element...\n")

  traverseLinkedList(element['next'])

if __name__ == '__main__':
  main()
