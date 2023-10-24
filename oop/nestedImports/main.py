from weapons.longsword import Longsword
from weapons.greatsword import Greatsword

def main():
  longsword = Longsword("Steel Longsword", 10, 5)

  greatsword = Greatsword("Adamant Greatsword", 28, 2)

  print(longsword)
  print(greatsword)

if __name__ == '__main__':
  main()
