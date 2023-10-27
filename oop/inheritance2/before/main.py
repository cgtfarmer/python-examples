from enemy import Enemy
from player import Player

def main():
  e1 = Enemy('Goblin', 30, 10, 5)

  e2 = Enemy('Black Knight', 50, 30, 18)

  p1 = Player('Acryce', 99, 99, 99, 99)

  p2 = Player('Anhphat', 45, 30, 25, 15)

  # c1 = Character('Uncle Deckard', 60, 10, 30)

  print(e1)
  print(e2)
  print(p1)
  print(p2)
  # print(c1)

  p2.setName('Arsidee')
  print('---')

  print(e1)
  print(e2)
  print(p1)
  print(p2)
  # print(c1)

  print('---')
  print(p1.calculateDmg())
  print(p2.calculateDmg())
  print(e1.calculateDmg())
  print(e2.calculateDmg())

if __name__ == '__main__':
  main()
