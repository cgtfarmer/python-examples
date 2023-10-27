from longsword import Longsword
from greatsword import Greatsword
from weirdsword import Weirdsword

def main():
  longsword = Longsword("Steel Longsword", 10, 5)

  greatsword = Greatsword("Adamant Greatsword", 28, 2)

  weirdsword = Weirdsword("Other Ditty", 44, 3, 99)

  print(longsword)
  print(greatsword)
  print(weirdsword)

if __name__ == '__main__':
  main()
