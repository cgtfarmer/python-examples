from player import Player

def main():
  player1 = Player('John', 'Doe', 100)
  print(player1)

  player2 = Player('Jane', 'Doe', 50)
  print(player2)

  print(player1.getXp())
  print(player2.getXp())

  print('---')
  player1.describe()
  player2.describe()

if __name__ == '__main__':
  main()
